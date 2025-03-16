from flask import Blueprint, request
from extentions import db
from models.user_model import User, UserSchema
from services.user_service import UserService

users_bp = Blueprint('users', __name__)

@users_bp.route("/")
def users():
    return {
        "message": "Users route is running!"
    }, 200

@users_bp.route("/register", methods=["POST"])
def register():
    try:
        data = request.json

        schema = UserSchema()
        user = schema.load(data)

        new_user = User(**user)

        UserService.create_user(new_user)

        return {
            "message": "User created successfully!"
        }, 201
    except Exception as e:
        return {
            "message": f"An error occurred while creating the user : {e}."
        }, 500