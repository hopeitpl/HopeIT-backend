from hopeit.actions.create_payment import CreatePaymentAction
from hopeit.api.resources import Resource, CallAction


class Payment(Resource):
    on_post = CallAction(CreatePaymentAction)
