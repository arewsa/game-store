from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from services.token import decode_jwt
from services.product import ProductService
from services.user import UserService

http_bearer = HTTPBearer()

def users_service():

    return UserService()

def product_service():
    return ProductService()

def authorize(credentials: HTTPAuthorizationCredentials = Depends(http_bearer)):
    try:
        access_token = credentials.credentials
        user_id = decode_jwt(json_web_token=access_token).get("user_id")
        return user_id
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    