from flask import g, current_app, make_response
from flask_restful import Resource

from app.auth.decorators import require_login
# from app.auth.session_manager import clear_session


class LogOutView(Resource):
    method_decorators = [require_login]

    def get(self):
        """Remove the current authenticated user session from the session store.."""
        
        response = make_response("Cookie Cleared")

        if hasattr(g, "user"):
            response.set_cookie('cookie_name', '', expires=0)
        

        redirect_url = current_app.config.get("LOGOUT_URL", "http://localhost")

        response = {"redirect_url": redirect_url}

        return response, 200
    
    # def get(self):
    #     """Remove the current authenticated user session from the session store.."""
    #     if hasattr(g, "user"):
    #         clear_session(g.user.id)

    #     redirect_url = current_app.config.get("LOGOUT_URL", "http://localhost")

    #     response = {"redirect_url": redirect_url}

    #     return response, 200
