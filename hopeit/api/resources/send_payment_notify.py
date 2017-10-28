from hopeit.actions.send_payment_notify import SendPaymentAction
from hopeit.api.resources import CallAction, Resource
from hopeit.api.schema.user import UserIdSchema


class Item(Resource):
    on_post = CallAction(SendPaymentAction, validator=UserIdSchema)
