from . import db
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    # social_id = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
