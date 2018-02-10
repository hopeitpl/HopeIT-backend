import json

from chaps import inject
from hopeit.core.models import Goal, User
from hopeit.core.models.payment import Payment
from hopeit.core.services.notifications.goal_completed import \
    GoalCompletedNotification
from hopeit.core.services.notifications.message import MessageNotification
from hopeit.core.services.notifications.payment_confirm import (
    PaymentNotificationConfirm)

from hopeit.actions.create_payment import CreatePaymentAction
from hopeit.actions.get_user_payments import GetUserPaymentsAction
from hopeit.api.resources import CallAction, Resource
from hopeit.core.models.message import Message


class CreatePayment(Resource):
    on_post = CallAction(CreatePaymentAction)


class Collection(Resource):
    on_get = CallAction(GetUserPaymentsAction)


@inject('db_session')
class PaymentUpdater:
    def run(self, req, resp):
        data = json.dumps(
            str(req.stream.read(), "utf-8")).replace('%40', '@').split('&')
        dict_data = dict(
            s.split('=') for s in [a.replace('"', '') for a in data])

        user_id_from_description_data = int(
            dict_data['description'].replace('%3A', ':').split(':')[1])
        active_goal = self.db_session.query(Goal).filter(
            Goal.finished.is_(False),
            Goal.user_id == user_id_from_description_data).first()

        payment = Payment(
            user_id=user_id_from_description_data,
            goal_id=active_goal.id if active_goal else active_goal,
            operation_number=dict_data['operation_number'],
            operation_type=dict_data['operation_type'],
            operation_status=dict_data['operation_status'],
            operation_amount=float(dict_data['operation_amount']),
            operation_currency=dict_data['operation_currency'],
            description=dict_data['description'],
            email=dict_data['email'],
            channel=int(dict_data['channel']),
            signature=dict_data['signature']
        )
        message = Message(
            user_id=user_id_from_description_data,
            message_type=Message.MESSAGE_TYPE_PAYMENT,
            body='Płatność została zrealizowana.',
        )
        self.db_session.add(payment)
        self.db_session.add(message)

        self.db_session.flush()

        user = self.db_session.query(User).filter(
            User.id == user_id_from_description_data).first()
        device_id = user.device
        if active_goal and active_goal.balance >= active_goal.target:
            active_goal.finished = True
            GoalCompletedNotification().send_single_device(device_id)
            message = Message(
                user_id=user.id,
                body="Gratulacje! Ukończyłeś założony cel!",
                picture='')
            # MessageNotification().send_single_device(device_id)
            self.db_session.add(message)

        PaymentNotificationConfirm().send_single_device(
            device_id, payment.operation_amount)
        MessageNotification().send_single_device(device_id)

        resp.body = 'OK'


class GetPaymentStatus(Resource):
    def on_post(self, req, resp):
        PaymentUpdater().run(req, resp)
