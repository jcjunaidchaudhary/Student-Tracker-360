from marshmallow import Schema,fields


class BasicDetailSchema(Schema):
    id = fields.Int(dump_only=True)
    contact2 = fields.Str()
    gender=fields.Str()
    dob=fields.Date()
    unique_id=fields.Str(dump_only=True)
    scholarship=fields.Str(dump_only=True)
    status=fields.Str(dump_only=True)
    photo=fields.Str(dump_only=True)
    user_id=fields.Int()
