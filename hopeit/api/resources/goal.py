from hopeit.actions.create_goal import CreateGoalAction
from hopeit.actions.get_goal import GetGoalAction
from hopeit.api.resources import CallAction, Resource


class Item(Resource):
    on_get = CallAction(GetGoalAction)
    on_post = CallAction(CreateGoalAction)
