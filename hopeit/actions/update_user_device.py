from chaps import inject

from hopeit.actions import Action
from hopeit.core.models import User


@inject('db_session')
class UpdateUserDeviceAction(Action):
    def do(self):
        user = self.db_session.query(User).filter(
            User.id == self.payload['user_id']).first()
        if user:
            user.device = self.payload['device_id']
