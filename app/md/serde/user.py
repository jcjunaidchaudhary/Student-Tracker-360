from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    email = fields.Str()
    phone1 = fields.Str()

    #
    disabled = fields.Boolean(dump_only=True)
    last_login = fields.Date(dump_only=True)

    modified_user_id = fields.Int(load_only=True)
    modified_on = fields.DateTime(load_only=True)
    modified_user = fields.Nested("UserSchema", only=("name", "id"), dump_only=True)
    modified_on = fields.Str(dump_only=True)
    modified_on_tmz = fields.Str(dump_only=True)
