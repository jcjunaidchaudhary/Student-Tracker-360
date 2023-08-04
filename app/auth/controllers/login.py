import datetime
from flask import abort, jsonify, make_response, request, session
from flask_restful import Resource
from app import app,db
from app.md.models.user import User
from app.md.serde.user import UserSchema
import jwt

class LoginView(Resource):
    
    def get(self):
        return {"Login":"Successful"}

    def post(self):
        """
        This login flow occurs when authenticating without SSO.

        Unlike the SSO flow, this endpoint is called as part of an
        AJAX request, and the client side will set the cookie.
        """
        credentials = request.get_json()

        if credentials.get("email"):
            user = User.query.filter_by(email=credentials["email"]).first()
        else:
            user = User.query.filter_by(phone1=credentials["phone1"]).first()

        if not user:
            abort(401)

        if user.disabled:
            abort(401)

        if not user.verify_password(credentials["password"]):
            abort(401)

        user.last_login = datetime.datetime.now()

        db.session.add(user)
        db.session.commit()

        # Retrieve and reuse active session id if user is a service account.
        session['user_id']=user.id

        
        if user.modified_user_id == -1:
            payload = {"user": UserSchema().dump(user), "is_admin": False,'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}
            token = jwt.encode(payload, app.config['SECRET_KEY'],algorithm="HS256")
        else:    
            payload = {"user": UserSchema().dump(user), "is_admin": True,'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}
            token = jwt.encode(payload, app.config['SECRET_KEY'],algorithm="HS256")

        response = make_response(token)
        response.set_cookie(
            "currentUser", token, secure=app.config.get("SECURE_COOKIE")
        )

        return response
