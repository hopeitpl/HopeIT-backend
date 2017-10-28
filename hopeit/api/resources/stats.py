from hopeit.actions.get_user_stats import GetUserStatsAction
from hopeit.api.resources import Resource, CallAction


class Item(Resource):
    on_get = CallAction(GetUserStatsAction)
