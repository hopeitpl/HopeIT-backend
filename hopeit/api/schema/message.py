from marshmallow import Schema, fields

from hopeit.api.schema.user import UserIdSchema


class MessageIdSchema(Schema):
    message_id = fields.Integer(required=True)


class MessageSchema(Schema):
    body = fields.String(required=True)
    picture = fields.String()
    user_ids = fields.List(fields.Integer())


class UserMessageIdSchema(UserIdSchema, MessageSchema):
    pass
