import string
import random

from utils.http_exceptions import DuplicationException, NotFoundException
from conference.services.auth_service import AuthService
from conference.models.user_model import User as UserModel
from conference.schemas.user_schema import UserCreate, UserUpdate
from conference.repositories.user_repo import UserRepo


class UserService:
    @classmethod
    def create_user(cls, user_in: UserCreate) -> UserModel:
        exists = UserRepo().check_exists_by_username(username=user_in.username)
        if exists:
            raise DuplicationException(detail="username")
        hashed_password = AuthService().get_password_hash(user_in.password)
        user_in.password = hashed_password
        return UserRepo().create_user(user_create=user_in)

    @classmethod
    def reset_password(cls, username: str):
        exists = UserRepo().check_exists_by_username(username=username)
        if not exists:
            raise NotFoundException(detail="username")
        user_model = UserRepo().get_user_by_username(username=username)
        letters = string.ascii_letters
        new_password = ''.join(random.choice(letters) for _ in range(8))
        new_hashed_password = AuthService().get_password_hash(new_password)
        user_update = UserUpdate(username=username, password=new_hashed_password)
        return UserRepo().update_user(user_model=user_model, user_update=user_update)

    @classmethod
    def get_user_by_username(cls, username: str):
        exists = UserRepo().check_exists_by_username(username=username)
        if not exists:
            raise NotFoundException(detail="username")
        return UserRepo().get_user_by_username(username=username)
