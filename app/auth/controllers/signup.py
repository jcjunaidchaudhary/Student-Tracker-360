from flask import g, request
import marshmallow
from app.exceptions import FPAPIException
from app.md.serde.user import UserSchema
from app.md.models.user import User
from app import db
from flask_restful import Resource



# Register or SignUp on Portal
class SignUpView(Resource):

    def get(self):
        return {"username":"hello"}

    def post(self):

        data = UserSchema(unknown=marshmallow.INCLUDE).load(request.get_json())
        existing_phone1 = User.query.filter_by(phone1=data["phone1"]).count()
        existing_email = User.query.filter_by(email=data["email"]).count()

        if existing_phone1:
            raise FPAPIException({"phone1": "Phone Number is already in use."})

        if existing_email:
            raise FPAPIException({"email": "Email is already in use."})

        user = User(**data)

        try:
            user.modified_user_id = g.user.id
        except AttributeError:
            user.modified_user_id = -1
        db.session.add(user)
        db.session.commit()
        return UserSchema().dump(user), 201