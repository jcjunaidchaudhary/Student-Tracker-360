from flask import g, request
import marshmallow
from app.auth.controllers.user_access import UserAccessView
from app.md.models.basic_detail import BasicDetail
from app import db
from app.md.serde.basic_detail import BasicDetailSchema


class BasicDetailView(UserAccessView):
    """To Insert, Update, Delete a Basic detail form"""

    def get(self):
        # detail=BasicDetail.query.filter_by(user_id=g.user.id).first()
        detail = BasicDetail.query.filter(BasicDetail.user_id == g.user.id).first()
        return BasicDetailSchema().dump(detail)

    def post(self):
        data = BasicDetailSchema(unknown=marshmallow.INCLUDE).load(request.get_json())
        data["user_id"] = g.user.id
        detail = BasicDetail(**data)

        db.session.add(detail)
        db.session.commit()
        return BasicDetailSchema().dump(detail)

    def put(self):
        data = request.get_json()

        BasicDetail.query.filter(BasicDetail.user_id == g.user.id).update(
            data, synchronize_session=False
        )
        db.session.commit()

        detail = BasicDetail.query.filter(BasicDetail.user_id == g.user.id).first()
        return BasicDetailSchema().dump(detail),201

    def delete(self):

        BasicDetail.query.filter(BasicDetail.user_id == g.user.id).delete()
        db.session.commit()

        return "", 201
