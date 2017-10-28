from marshmallow import fields, Schema

from hopeit.api.schema.user import UserIdSchema


class MessageIdSchema(Schema):
    message_id = fields.Integer(required=True)


class MessageSchema(Schema):
    body = fields.String(required=True)
    picture = fields.String()


class UserMessageIdSchema(UserIdSchema, MessageSchema):
    pass
