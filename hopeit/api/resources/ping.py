from marshmallow import fields, Schema

from hopeit.actions.ping import PingAction
from hopeit.api.resources import CallAction, Resource


class PingSchema(Schema):
    field = fields.String()
    num = fields.Number()


class Ping(Resource):
    on_get = CallAction(PingAction)

    on_post = CallAction(PingAction, validator=PingSchema)
