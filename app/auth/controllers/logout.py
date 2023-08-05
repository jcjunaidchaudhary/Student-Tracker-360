from flask import current_app, jsonify, request
from flask_restful import Resource

from app.auth.decorators import require_login
# from app.auth.session_manager import clear_session

# Keep a blacklist of invalidated tokens
token_blacklist = set()

class LogOutView(Resource):
    method_decorators = [require_login]

    def get(self):
        """Remove the current authenticated user session from the session store.."""
        token = request.cookies.get('currentUser')

        if token:
            # Add the token to the blacklist by setting its expiration to a past date
            token_blacklist.add(token)
            # Create a response to clear the cookie on the client-side
            redirect_url = current_app.config.get("LOGOUT_URL", "http://localhost")

            response = jsonify(message='Logged out successfully',redirect_url=redirect_url)
            response.delete_cookie('currentUser')

            return response

        return jsonify(message='No token found'), 400
        
