from repositories.user_repository import UserRepository
from models.user_model import User


class UserService:
    @staticmethod
    def create_user(user: User):
        is_exists = UserRepository.get_user_by_email(user.email)

        if is_exists:
            return False

        UserRepository.create_user(user)


        return True