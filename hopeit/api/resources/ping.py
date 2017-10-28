from marshmallow import fields, Schema

from hopeit.actions.ping import PingAction
from hopeit.api.resources import CallAction, Resource
from hopeit.api.hooks.authorization import authorize_user


class PingSchema(Schema):
    field = fields.String()
    num = fields.Number()


class Ping(Resource):
    on_get = authorize_user(CallAction(PingAction))

    on_post = CallAction(PingAction, validator=PingSchema)
