import bcrypt
from fastapi import HTTPException
from schemas.user import UserLogin
from schemas.token import Tokens
from services.token import get_tokens
from services.user import UserService
from sqlalchemy.ext.asyncio import AsyncSession


async def authenticate(user: UserLogin, user_service: UserService, session: AsyncSession) -> Tokens:
    user_orm = await user_service.get_by_mail(user.mail, session)
    if user_orm is None:
        raise HTTPException(status_code=400, detail="User not found")
    if not bcrypt.checkpw(password=user.password.encode(), hashed_password=user_orm.password.encode()):
        raise HTTPException(status_code=400, detail="Invalid password")
    return get_tokens(user_id=user_orm.id)
