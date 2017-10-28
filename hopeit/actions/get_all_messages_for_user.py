from chaps import inject
from hopeit.actions import Action

from hopeit.models.message import Message


@inject('db_session')
class GetAllMessagesForUser(Action):

    def get_all_messages_for_user(self, user_id):
        return self.db_session.query(Message).filter(
            Message.user_id == user_id)

    def do(self):
        return {'messages': [{
            'id': m.id,
            'body': m.body,
            'picture': m.picture,
            'date': str(m.date)
        } for m in self.get_all_messages_for_user(self.payload['user_id'])]}
