from chaps import inject

from hopeit.actions import Action
from hopeit.core.models.goal import Goal
from hopeit.core.models.message import Message
from hopeit.core.models.user import User
from hopeit.core.services.notifications.payment import PaymentNotification


@inject('db_session')
class SendPaymentAction(Action):

    def do(self):
        user_id = self.payload['user_id']
        message = Message(
            user_id=user_id,
            body='Zbliża się pora spłaty')
        user = self.db_session.query(User).filter(User.id == user_id).first()
        goal = self.db_session.query(Goal).filter(
            Goal.finished.is_(False)).first()
        PaymentNotification().send_single_device(user.device,
                                                 goal.next_installment_amount)

        self.db_session.add(message)
