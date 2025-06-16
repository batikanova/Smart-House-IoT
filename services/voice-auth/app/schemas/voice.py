
from marshmallow import Schema, fields, validate

class voiceSchema(Schema):

    name = fields.Str(required=True)
    email = fields.Email(required=True)
class verifySchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(min=1, max=255))