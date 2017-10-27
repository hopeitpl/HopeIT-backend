from chaps import inject
from hopeit.actions import Action

from hopeit.models.user import User


@inject('db_session')
class GetAllUsersAction(Action):

    def get_all_users(self):
        return self.db_session.query(User).all()

    def do(self):
        return {'users': [{
            'id': u.id,
            'username': u.username,
            'device': u.device
        } for u in self.get_all_users()]}
