from flask import g, request
import marshmallow
from marshmallow.exceptions import ValidationError
from app.auth.controllers.user_access import UserAccessView
from app.md.models.education_detail import Education
from app import db
from app.md.serde.education_detail import EducationSchema
from app.exceptions import FPAPIException


class EducationView(UserAccessView):
    """To Read, Insert, Update, Delete a Current Education form"""

    def get(self):
        curr_edu = Education.query.filter(Education.user_id == g.user.id)
        return EducationSchema(many=True).dump(curr_edu)

    def post(self):
        data = EducationSchema(unknown=marshmallow.INCLUDE).load(
            request.get_json()
        )
        data["user_id"] = g.user.id
        data["result"] = (data["marks_obtained"] / data["total_marks"]) * 100
        curr_edu = Education(**data)

        db.session.add(curr_edu)
        db.session.commit()
        return EducationSchema().dump(curr_edu)

    def put(self):
        data = request.get_json()
        data["result"] = (data["marks_obtained"] / data["total_marks"]) * 100

        try:
            curr_edu = EducationSchema().load(data, unknown=marshmallow.EXCLUDE)
        except ValidationError as error:
            raise FPAPIException(error.messages)

        Education.query.filter(Education.id == curr_edu["id"]).update(
            curr_edu, synchronize_session=False
        )

        db.session.commit()
        curr_edu = Education.query.get(curr_edu["id"])
        return EducationSchema().dump(curr_edu), 201

    def delete(self):

        data = request.get_json()

        Education.query.filter(
            Education.id.in_([f["id"] for f in data])
        ).delete()

        db.session.commit()

        return "", 201
