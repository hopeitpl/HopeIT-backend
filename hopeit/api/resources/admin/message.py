from hopeit.actions.create_message_for_all_users import CreateMessageForUsers
from hopeit.actions.get_all_messages import GetAllMessages
from hopeit.actions.get_message import GetMessage
from hopeit.api.hooks.authorization import authorize_user
from hopeit.api.resources import CallAction, Resource
from hopeit.api.schema.message import MessageIdSchema, MessageSchema


class Item(Resource):
    on_get = authorize_user(CallAction(GetMessage, validator=MessageIdSchema))


class Collection(Resource):
    on_post = authorize_user(CallAction(CreateMessageForUsers,
                                        validator=MessageSchema))
    on_get = authorize_user(CallAction(GetAllMessages))
