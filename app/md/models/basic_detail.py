from app import db


class BasicDetail(db.Model):
    __tablename__ = "basic_detail"
    __table_args__ = (
        db.CheckConstraint("length(contact2)=10 ", name="contact2_check"),
        db.UniqueConstraint("user_id"),
    )
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String)
    dob = db.Column(db.Date(), nullable=False)
    contact2 = db.Column(db.String, default="")
    unique_id = db.Column(db.String, default="")
    scholarship = db.Column(db.String, default="", nullable=False)
    status = db.Column(db.String, default="")
    photo = db.Column(db.String, nullable=False, default="")
    user_id = db.Column(
        "user_id",
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE"),
    )
