from hopeit.actions.get_user import GetUserAction
from hopeit.actions.get_all_users import GetAllUsersAction
from hopeit.api.resources import CallAction, Resource
from hopeit.api.hooks.authorization import authorize_user


class Item(Resource):
    on_get = authorize_user(CallAction(GetUserAction))


class Collection(Resource):
    on_get = authorize_user(CallAction(GetAllUsersAction))
