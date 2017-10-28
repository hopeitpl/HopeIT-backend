import json
from datetime import datetime

from chaps import Inject

from hopeit.actions.create_payment import CreatePaymentAction
from hopeit.api.resources import CallAction, Resource
from hopeit.models import Goal, User
from hopeit.models.payment import Payment


class CreatePayment(Resource):
    on_post = CallAction(CreatePaymentAction)


class GetPaymentStatus(Resource):
    db_session = Inject('db_session')

    def on_post(self, req, _):
        data = json.dumps(
            str(req.stream.read(), "utf-8")).replace('%40', '@').split('&')
        dict_data = dict(
            s.split('=') for s in [a.replace('"', '') for a in data])

        user_id_from_description_data = int(
            dict_data['description'].replace('%3A', ':').split(':')[1])
        active_goal = self.db_session.query(Goal).filter(
            Goal.finished.is_(False),
            Goal.user_id==user_id_from_description_data).first()

        payment = Payment(
            user_id=user_id_from_description_data,
            goal_id=active_goal.id if active_goal else active_goal,
            operation_number=dict_data['operation_number'],
            operation_type=dict_data['operation_type'],
            operation_status=dict_data['operation_status'],
            operation_amount=float(dict_data['operation_amount']),
            operation_currency=dict_data['operation_currency'],
            operation_datetime=datetime.now(),
            description=dict_data['description'],
            email=dict_data['email'],
            channel=int(dict_data['channel']),
            signature=dict_data['signature']
        )

        self.db_session.add(payment)

        return {
            'results': 'OK'
        }
