from hopeit.actions.get_all_messages_for_user import GetAllMessagesForUser
from hopeit.api.resources import CallAction, Resource
from hopeit.api.schema.user import UserIdSchema


class Item(Resource):
    on_get = CallAction(GetAllMessagesForUser, validator=UserIdSchema)
