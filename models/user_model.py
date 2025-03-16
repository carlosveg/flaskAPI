import datetime

from marshmallow import Schema, fields, validate
from extentions import bcrypt

from extentions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), default=datetime.datetime.now())

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class UserSchema(Schema):
    name = fields.String(
        required=True,
        validate=validate.Length(min=3, max=100)
    )
    email = fields.Email(
        required=True,
        validate=validate.Length(max=100, error="Email cannot be more than 100 characters")
    )
    password = fields.String(
        required=True,
        validate=validate.Length(min=8, max=100)
    )