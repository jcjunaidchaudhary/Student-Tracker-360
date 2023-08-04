from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.md.models.base import BaseAuditModel


class User(BaseAuditModel):
    __tablename__ = "user"
    __table_args__ = (
        db.CheckConstraint(
            "length(name) >= 3 AND length(name) <= 64", name="user_name_check"
        ),
        db.CheckConstraint(
            "length(username) >= 3 AND length(username) <= 32",
            name="user_username_check",
        ),
        db.CheckConstraint(
            "length(email) >= 3 AND length(email) <= 64", name="user_email_check"
        ),
        db.CheckConstraint("length(phone1)=10 ", name="phone1_check"),
        
        db.UniqueConstraint("email"),
        db.UniqueConstraint("phone1"),
    )

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    _password = db.Column(db.String, nullable=True)

    # Client Logo
    # profile_img_path = db.Column(db.String(256), default="", nullable=True)

    # Email address where users should receive emails
    email = db.Column(db.String, nullable=True)
    phone1 = db.Column(db.String, default="", nullable=True)

    disabled = db.Column(db.Boolean, default=False, nullable=True)
    last_login = db.Column(db.Date, nullable=True)

    modified_on = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now(),
        default=db.func.now(),
    )

    @property
    def password(self):
        """Reading the plaintext password value is not possible or allowed."""
        raise AttributeError("cannot read password")

    @password.setter
    def password(self, password):
        """
        Intercept writes to the `password` attribute and hash the given
        password value.
        """
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        """
        Accept a password and hash the value while comparing the hashed
        value to the password hash contained in the database.
        """
        return check_password_hash(self._password, password)
