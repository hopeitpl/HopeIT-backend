from hopeit.actions.get_user_payments import GetUserPaymentsAction
from hopeit.api.hooks.authorization import authorize_user
from hopeit.api.resources import CallAction, Resource


class Collection(Resource):
    on_get = authorize_user(CallAction(GetUserPaymentsAction))
