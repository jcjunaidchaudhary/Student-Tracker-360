from flask import Blueprint
from flask_restful import Api

from app.md.controllers.basic_detail import BasicDetailView
from app.md.controllers.education_detail import EducationView


common_blueprint = Blueprint("common", __name__, url_prefix="/common")
api = Api(common_blueprint)

api.add_resource(BasicDetailView, "/basicdetail/")
api.add_resource(EducationView, "/educationdetail/")
