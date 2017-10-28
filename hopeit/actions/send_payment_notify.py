from chaps import inject

from hopeit.actions import Action
from hopeit.models.message import Message
from hopeit.models.user import User
from hopeit.services.notifications.payment import PaymentNotification


@inject('db_session')
class SendPaymentAction(Action):

    def do(self):
        user_id = self.payload['user_id']
        message = Message(
            user_id=user_id,
            body='Zbliża się pora spłaty')
        user = self.db_session.query(User).filter(User.id == user_id).first()
        PaymentNotification().send_single_device(user.device)

        self.db_session.add(message)
