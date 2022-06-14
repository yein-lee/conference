from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from pydantic import ValidationError

from fastapi.security import OAuth2PasswordRequestForm

from utils.http_exceptions import \
    (NotFoundException,
     InvalidPasswordException,
     JWTDecodeException,
     ValidationException)
from config.settings import Settings
from config.security import ALGORITHM, pwd_context
from conference.models.user_model import User as UserModel
from conference.schemas.token_schema import Token, TokenData
from conference.repositories.user_repo import UserRepo


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return pwd_context.hash(password)

    @classmethod
    def authenticate(cls, username: str, password: str) -> Optional[UserModel]:
        exists = UserRepo().check_exists_by_username(username=username)
        if not exists:
            raise NotFoundException(detail='User')
        user_model = UserRepo().get_user_by_username(username=username)
        if not cls.verify_password(password, user_model.password):
            raise InvalidPasswordException()
        return user_model

    @classmethod
    def create_access_token(cls, form_data: OAuth2PasswordRequestForm) -> Token:
        user_model = cls.authenticate(username=form_data.username, password=form_data.password)
        access_token_expires = timedelta(minutes=Settings().ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.utcnow() + access_token_expires
        to_encode = {"exp": expire, "sub": user_model.username}
        access_token = jwt.encode(to_encode, Settings().SECRET_KEY, algorithm=ALGORITHM)
        token = Token(access_token=access_token, token_type="bearer")
        return token

    @classmethod
    def get_username_from_token(cls, token: str) -> str:
        try:
            decoded_jwt = jwt.decode(token, Settings().SECRET_KEY, algorithms=[ALGORITHM])
            token_data = TokenData(**decoded_jwt)
            username = token_data.sub
        except JWTError:
            raise JWTDecodeException()
        except ValidationError:
            raise ValidationException()
        return username
