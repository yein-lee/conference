from enum import Enum
from pydantic import EmailStr
from typing import Optional
from conference.schemas.base_schema import BaseSchema


class UserLevel(str, Enum):
    owner = 'owner'
    member = 'member'


class UserCreateDTO(BaseSchema):
    username: EmailStr
    name: str
    password: str


class UserResetPasswordDTO(BaseSchema):
    username: EmailStr


class UserUpdateDTO(BaseSchema):
    name: Optional[str] = None
    password: Optional[str] = None
