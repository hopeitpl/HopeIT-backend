from chaps import inject

from hopeit.actions import Action
from hopeit.core.models.message import Message


@inject('db_session')
class GetMessage(Action):

    def get_message(self, message_id):
        return self.db_session.query(Message).filter(
            Message.id == message_id).first()

    def do(self):
        message_id = self.payload['message_id']
        message = self.get_message(message_id)
        if message:
            return message.to_dict()
