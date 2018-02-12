from hopeit.actions.create_message_for_user import CreateMessageForUser
from hopeit.actions.get_all_messages_for_user import GetAllMessagesForUser
from hopeit.api.hooks.authorization import authorize_user
from hopeit.api.resources import CallAction, Resource
from hopeit.api.schema.message import UserMessageIdSchema
from hopeit.api.schema.user import UserIdSchema


class Item(Resource):
    on_post = authorize_user(CallAction(CreateMessageForUser,
                                        validator=UserMessageIdSchema))
    on_get = authorize_user(CallAction(GetAllMessagesForUser,
                                       validator=UserIdSchema))
