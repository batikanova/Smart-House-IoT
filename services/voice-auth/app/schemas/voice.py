
from marshmallow import Schema, fields, validate

class voiceSchema(Schema):

    userName = fields.Str(required=True)
    userMail = fields.Email(required=True)
