from functools import wraps
from flask import jsonify, request, session
from app.md.models.user import User
from app import app
import jwt


def require_login(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        token=request.cookies.get('currentUser')
        

        if not token:
            return jsonify({'message' : 'Token is missing!'})
        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"],options=None)
            current_user = User.query.filter_by(id=data['user_id']).first()
            if current_user.id != session["user_id"]:
                return jsonify({'message' : 'Token is invalid!'})
        except:
            return jsonify({'message' : 'Token is invalid!'})

        return f(current_user)
    return decorated
