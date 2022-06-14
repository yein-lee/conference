from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from conference.services.auth_service import AuthService
from conference.schemas.token_schema import Token

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    return await AuthService().create_access_token(form_data)
