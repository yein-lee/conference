from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from conference.services.auth_service import AuthService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_username_of_current_user(
        token: str = Depends(oauth2_scheme),
) -> str:
    return AuthService.get_username_from_token(token)
