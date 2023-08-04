from app import db


class Education(db.Model):
    __tablename__ = "current_education"
    __table_args__ = (
        db.CheckConstraint("length(college_number) = 10", name="college_number_check"),
        db.CheckConstraint("length(person_number) = 10", name="person_number_check"),
    )

    id = db.Column(db.Integer, primary_key=True)

    admission_year = db.Column(db.Integer, nullable=False)
    qualification_level = db.Column(db.String, nullable=False)
    board = db.Column(db.String)
    stream = db.Column(db.String(50), nullable=False)
    college = db.Column(db.String, nullable=False)
    course = db.Column(db.String, nullable=False)
    year_of_study = db.Column(db.String(30), nullable=False)
    mode = db.Column(db.String(30))
    is_complete = db.Column(db.Boolean, default=False, server_default="f")

    college_number = db.Column(db.String, nullable=False)
    contact_person = db.Column(db.String, nullable=False)
    designation = db.Column(db.String, nullable=False)
    person_number = db.Column(db.String, nullable=False)

    marks_obtained = db.Column(db.Integer, nullable=False)
    total_marks = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Numeric(10, 2), nullable=False)

    user_id = db.Column(
        "user_id",
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE"),
    )

    supported_doc = db.Column(db.String)

    modified_on = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now(),
        default=db.func.now(),
    )
    user = db.relationship("User")
