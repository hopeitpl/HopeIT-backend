from hopeit.actions.create_goal import CreateGoalAction
from hopeit.api.resources import Resource, CallAction


class Item(Resource):
    on_post = CallAction(CreateGoalAction)
