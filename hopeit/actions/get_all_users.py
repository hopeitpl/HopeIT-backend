from chaps import inject

from hopeit.actions import Action
from hopeit.core.models import User


@inject('db_session')
class GetAllUsersAction(Action):

    def get_all_users(self):
        return self.db_session.query(User).all()

    def do(self):
        return {'users': [u.to_dict() for u in self.get_all_users()]}
