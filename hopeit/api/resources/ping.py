from hopeit.actions.ping import PingAction
from hopeit.api.resources import CallAction, Resource


class Ping(Resource):
    on_get = CallAction(PingAction)
