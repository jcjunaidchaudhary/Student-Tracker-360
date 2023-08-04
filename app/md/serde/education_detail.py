from marshmallow import Schema, fields



class EducationSchema(Schema):
    id = fields.Int()
    admission_year = fields.Int()
    qualification_level = fields.Str()
    board = fields.Str()
    stream = fields.Str()
    college = fields.Str()
    course = fields.Str()
    year_of_study = fields.Str()
    mode = fields.Str()
    is_complete = fields.Boolean()

    college_number = fields.Str()
    contact_person = fields.Str()
    designation = fields.Str()
    person_number = fields.Str()

    marks_obtained = fields.Int()
    total_marks = fields.Int()
    result = fields.Decimal(2, as_string=True)

    user_id = fields.Int()

    supported_doc = fields.Str()
    user = fields.Nested("UserSchema", only=("name", "id"), dump_only=True)
    modified_on = fields.Str(dump_only=True)
