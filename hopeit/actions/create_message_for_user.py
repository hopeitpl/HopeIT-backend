from chaps import inject

from hopeit.actions import Action
from hopeit.models.message import Message
from hopeit.models.user import User
from hopeit.services.notifications.message import MessageNotification


@inject('db_session')
class CreateMessageForUser(Action):

    def do(self):
        user_id = self.payload['user_id']
        message = Message(
            user_id=user_id,
            body=self.payload['body'],
            picture=self.payload.get('picture', ''))
        user = self.db_session.query(User).filter(User.id == user_id).first()
        MessageNotification().send_single_device(user.device)

        self.db_session.add(message)
