from chaps import inject
from sqlalchemy import or_

from hopeit.actions import Action

from hopeit.models.message import Message


@inject('db_session')
class GetAllMessagesForUser(Action):

    def get_all_messages_for_user(self, user_id):
        return self.db_session.query(Message).filter(
            or_(
                Message.user_id == user_id,
                Message.user_id.is_(None)
            )).order_by(Message.date.desc())

    def do(self):
        return {'messages': [m.to_dict() for m in
                             self.get_all_messages_for_user(
                                 self.payload['user_id'])]}
