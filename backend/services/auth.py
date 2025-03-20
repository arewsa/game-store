import bcrypt
from fastapi import HTTPException
from schemas.token import Tokens
from services.token import get_tokens
from services.user import UserService
from schemas.user import UserLoginAndPassword, UserInSystem, UserLoginAndId


def authenticate(user: UserLoginAndPassword, user_service: UserService) -> Tokens:
    user_in_system: UserInSystem = user_service.get_user(email = user.login)
    if not bcrypt.checkpw(password=user.password.encode(), hashed_password=user_in_system.password.encode()):
        raise HTTPException(status_code=400, detail="Invalid login or password")
    user_password_and_id = UserLoginAndId(user_id=user_in_system.user_id, login=user_in_system.login)
    return get_tokens(user_id=user_password_and_id.user_id)

    