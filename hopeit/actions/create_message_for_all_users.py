from chaps import inject

from hopeit.actions import Action
from hopeit.core.models.message import Message
from hopeit.core.models.user import User
from hopeit.core.services.notifications.message import MessageNotification


@inject('db_session')
class CreateMessageForUsers(Action):

    def do(self):
        user_ids = self.payload.get('user_ids')

        if user_ids:
            for u_id in user_ids:
                message = Message(body=self.payload['body'],
                                  picture=self.payload.get('picture', ''),
                                  user_id=u_id)
                self.db_session.add(message)
            users = self.db_session.query(
                User).filter(User.id.in_(user_ids))
        else:
            message = Message(body=self.payload['body'],
                              picture=self.payload.get('picture', ''))
            users = self.db_session.query(User).all()
            self.db_session.add(message)

        mobile_device_ids = [u.device for u in users]
        MessageNotification().send_multiple_devices(mobile_device_ids)
