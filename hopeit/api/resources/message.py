from hopeit.actions.get_message import GetMessage
from hopeit.api.resources import CallAction, Resource
from hopeit.api.schema.message import MessageIdSchema


class Item(Resource):
    on_get = CallAction(GetMessage, validator=MessageIdSchema)
