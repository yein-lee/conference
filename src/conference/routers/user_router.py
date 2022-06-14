from fastapi import APIRouter, Body
from conference.services.user_service import UserService
from conference.services.mail_service import MailService
from conference.schemas.user_schema import User, UserCreate, UserResetPassword

router = APIRouter()


@router.post("/register", response_model=User)
def register(user_in: UserCreate = Body(...)) -> User:
    return UserService().create_user(user_in)


@router.post("/reset-password", response_model=User)
def reset_password(user: UserResetPassword = Body(...)) -> User:
    complete_reset_password_user = UserService().reset_password(username=user.username)
    message = MailService().build_password_message(to=user.username, new_password=complete_reset_password_user.password)
    MailService().send(message)
    return complete_reset_password_user
