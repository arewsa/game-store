from fastapi import APIRouter, Cookie, Depends, Response
from fastapi.security import HTTPBearer
from services.token import refresh_tokens
from schemas.token import Tokens
from services.auth import authenticate
from web.routes.dependencies import authorize, users_service
from services.user import UserService
from schemas.user import CreateUser, UserLoginAndPassword

http_bearer = HTTPBearer()

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", status_code=200)
async def registration(user: CreateUser, user_service: UserService = Depends(users_service)):
    return user_service.add_user(user)

@router.get("/", status_code=200)
async def get_user(user_mail: str, user_service: UserService = Depends(users_service)):
    return user_service.get_user(user_mail)

@router.get("/all", status_code=200)
async def get_users(user_service: UserService = Depends(users_service)):
    return user_service.get_all_users()

@router.post("/authentication", status_code=200)
async def auth(response: Response, user: UserLoginAndPassword, user_service: UserService = Depends(users_service)):
    tokens: Tokens = authenticate(user, user_service)
    response.set_cookie(key="refresh_token", value=tokens.refresh_token, httponly=True)
    return {
        "access_token": tokens.access_token,
        "token_type": "Bearer"
       }

@router.get("/refresh", status_code=200)
async def refresh( response: Response, refresh_token: str = Cookie()):
    tokens: Tokens = refresh_tokens(refresh_token)
    response.set_cookie(key="refresh_token", value=tokens.refresh_token, httponly=True)
    return {
        "access_token": tokens.access_token,
        "token_type": "Bearer"
       }

@router.get("/login", status_code=200)
async def login(user_id: int = Depends(authorize)):
    return user_id