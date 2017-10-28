from marshmallow import fields, Schema


class UserIdSchema(Schema):
    user_id = fields.Integer(required=True)