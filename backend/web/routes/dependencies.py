from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from services.token import decode_jwt
from models.product import TableGame
from repository.product_repository import ProductRepository
from services.product import ProductService
from repository.user_repository import UserRepository
from services.user import UserService

http_bearer = HTTPBearer()

def users_service():

    return UserService(UserRepository())

def game_service():
    return ProductService(ProductRepository(TableGame))

def authorize(credentials: HTTPAuthorizationCredentials = Depends(http_bearer)):
    try:
        access_token = credentials.credentials
        user_id = decode_jwt(json_web_token=access_token).get("user_id")
        return user_id
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")