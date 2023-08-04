import datetime
from flask import abort, jsonify, make_response, request, session
from flask_restful import Resource
from app import app
from app.md.models.user import User
from app.md.serde.user import UserSchema
import jwt

class LoginView(Resource):
    
    def get(self):
        return {"Login":"Successful"}

    def post(self):
        
        credentials = request.get_json()
        user=User.query.filter_by(username=credentials["username"]).first()
        session['user_id']=user.id
        if not user:
            abort(401)

        if not user.verify_password(credentials["password"]):
            abort(401)

        token = jwt.encode({'user_id' : user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}, app.config['SECRET_KEY'],algorithm="HS256")

        response = make_response(token)
        response.set_cookie(
            "currentUser", token, secure=app.config.get("SECURE_COOKIE")
        )
        return response
