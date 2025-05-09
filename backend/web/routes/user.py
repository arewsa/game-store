from fastapi import APIRouter, Cookie, Depends, HTTPException, Request, Response
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from models.user import UsersORM
from services.token import refresh_tokens
from schemas.token import Tokens
from services.auth import authenticate
from web.routes.dependencies import authorize, users_service
from services.user import UserService
from schemas.user import CreateUser, User, UserLogin
from sqlalchemy.ext.asyncio import AsyncSession
from models.database import db_helper

http_bearer = HTTPBearer()

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("", status_code=200)
async def registration(user: CreateUser, user_service: UserService = Depends(users_service), session: AsyncSession = Depends(db_helper.get_session)):
    result: UsersORM | None = await user_service.add(user, session)
    if result is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return User.model_validate(result)

@router.get("/me", status_code=200)
async def get_user (user_id: int = Depends(authorize), user_service: UserService = Depends(users_service), session: AsyncSession = Depends(db_helper.get_session), credentials: HTTPAuthorizationCredentials = Depends(http_bearer)):
    result = await user_service.get_by_id(user_id, session)
    return User.model_validate(result)

@router.post("/login", status_code=200)
async def auth(response: Response, user: UserLogin, user_service: UserService = Depends(users_service), session: AsyncSession = Depends(db_helper.get_session)):
    tokens: Tokens = await authenticate(user, user_service, session)
    response.set_cookie(key="refresh_token", value=tokens.refresh_token, httponly=True, samesite="lax", secure=False)
    return {
        "access_token": tokens.access_token,
        "token_type": "Bearer"
       }

@router.get("/refresh", status_code=200)
async def refresh(response: Response, refresh_token: str = Cookie()):
    tokens: Tokens = refresh_tokens(refresh_token)
    response.set_cookie(key="refresh_token", value=tokens.refresh_token, httponly=True, samesite="none", secure=True)
    return {
        "access_token": tokens.access_token,
        "token_type": "Bearer"
       }