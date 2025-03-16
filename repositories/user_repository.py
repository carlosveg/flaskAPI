from extentions import db
from models.user_model import User


class UserRepository:
    @staticmethod
    def create_user(user) -> None:
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_by_email(email) -> User:
        return User.query.filter_by(email=email).first()
