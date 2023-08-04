from sqlalchemy.ext.declarative import AbstractConcreteBase, declared_attr
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
import pytz
from flask import g
from app import db


class BaseAuditModel(AbstractConcreteBase, db.Model):
    __abstract__ = True
    modified_on = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now(),
        default=db.func.now(),
        onupdate=db.func.now(),
    )

    @declared_attr
    def modified_user_id(cls):
        return Column(ForeignKey("user.id"))

    @declared_attr
    def modified_user(cls):
        fk = "{}.modified_user_id".format(cls.__name__)
        return relationship("User", foreign_keys=fk)

    @property
    def modified_on_tmz(self):
        est = pytz.timezone("Asia/Calcutta")
        fmt = "%Y-%m-%d %H:%M"
        return self.modified_on.astimezone(est).strftime(fmt)

    def set_current_user(self):
        if hasattr(g, "user") and g.user:
            user_id = g.user.id
            self.modified_user_id = user_id
        if self.modified_user_id is None:
            self.modified_user_id = -1

