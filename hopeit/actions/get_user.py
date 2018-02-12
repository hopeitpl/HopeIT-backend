from chaps import inject

from hopeit.actions import Action
from hopeit.core.models import User


@inject('db_session')
class GetUserAction(Action):

    def get_user(self, user_id):
        return self.db_session.query(User).filter(
            User.id == user_id).first()

    def do(self):
        user_id = self.payload['user_id']
        user = self.get_user(user_id)
        if user:
            return user.to_dict()
