from flask import Blueprint
from flask_restful import Api

from app.md.controllers.basic_detail import BasicDetailView
from app.md.controllers.education_detail import EducationView


md_blueprint = Blueprint("md", __name__, url_prefix="/md")
api = Api(md_blueprint)

api.add_resource(BasicDetailView, "/basicdetail/")
api.add_resource(EducationView, "/educationdetail/")
