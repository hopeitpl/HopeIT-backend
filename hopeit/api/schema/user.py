from marshmallow import Schema, fields


class UserIdSchema(Schema):
    user_id = fields.Integer(required=True)
