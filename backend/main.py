from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, Response, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import databaseFunction
import authFunc
from config import Status
from fastapi.security import HTTPBearer

http_bearer = HTTPBearer()

app = FastAPI()

origins = ["http://localhost", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




class User(BaseModel):
    name: str
    surname: str
    mail: str
    password: str

class UserLoginAndPassword(BaseModel):
    login: str
    password: str

class TokenInfo(BaseModel):
    access_token: str
    token_type: str


@app.post("/users")
async def create_user(user: User):
    return {"status": databaseFunction.add_new_user(user.name, user.surname, user.mail, user.password)}


@app.get("/games")
async def get_games():
    return databaseFunction.get_all_game_cards()


@app.post("/login")
async def auth_login(response: Response, user_info: UserLoginAndPassword):
    if authFunc.auth_login_check(user_info.login, user_info.password) == Status.OK:
        jwt_payload = {
            "sub": databaseFunction.get_user_id(user_info.login),
            "username": user_info.login,
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
        }
        token = authFunc.encode_jwt(jwt_payload)
        response.set_cookie(key="test", value="lol", samesite="none")
        return TokenInfo(
            access_token=token,
            token_type="Bearer",
        )
    else:
        response.status_code=401
        return {"status": Status.AuthError.value}
