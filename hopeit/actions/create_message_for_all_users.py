from chaps import inject

from hopeit.actions import Action
from hopeit.models.user import User
from hopeit.models.message import Message
from hopeit.services.notifications.message import MessageNotification


@inject('db_session')
class CreateMessageForUsers(Action):

    def do(self):
        message = Message(body=self.payload['body'],
                          picture=self.payload.get('picture', ''))
        users = self.db_session.query(User).all()
        mobile_device_ids = [u.device for u in users]
        MessageNotification().send_multiple_devices(mobile_device_ids)

        self.db_session.add(message)
