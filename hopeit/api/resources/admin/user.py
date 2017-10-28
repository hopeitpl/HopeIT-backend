from marshmallow import fields, Schema

from hopeit.actions.get_user import GetUserAction
from hopeit.actions.get_all_users import GetAllUsersAction
from hopeit.api.resources import CallAction, Resource
from hopeit.api.hooks.authorization import authorize_user


class UserIdSchema(Schema):
    user_id = fields.Integer(required=True)


class Item(Resource):
    on_get = authorize_user(CallAction(GetUserAction, validator=UserIdSchema))


class Collection(Resource):
    on_get = authorize_user(CallAction(GetAllUsersAction))
