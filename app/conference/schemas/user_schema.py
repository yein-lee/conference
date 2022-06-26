from enum import Enum
from pydantic import EmailStr
from typing import Optional
from conference.schemas.base_schema import BaseSchema


class UserLevel(str, Enum):
    owner = 'owner'
    member = 'member'


class User(BaseSchema):
    id: int
    username: EmailStr
    name: str
    password: str


class UserCreate(BaseSchema):
    username: EmailStr
    name: str
    password: str


class UserResetPassword(BaseSchema):
    username: EmailStr


class UserUpdate(BaseSchema):
    name: str = None
    password: Optional[str] = None
