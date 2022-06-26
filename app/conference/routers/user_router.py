from fastapi import APIRouter, Body
from conference.services.user_service import UserService
from conference.services.mail_service import MailService
from conference.models.user_model import UserModel
from conference.schemas.user_schema import UserCreate, UserResetPassword

router = APIRouter()


@router.post("/register", response_model=UserModel)
async def register(user_in: UserCreate = Body(...)) -> UserModel:
    user_model = await UserService().create_user(user_in=user_in)
    return user_model


@router.post("/reset-password", response_model=UserModel)
async def reset_password(user: UserResetPassword = Body(...)) -> UserModel:
    complete_reset_password_user = await UserService().reset_password(username=user.username)
    message = MailService().build_password_message(to=user.username, new_password=complete_reset_password_user.password)
    MailService().send(message)
    return await complete_reset_password_user
