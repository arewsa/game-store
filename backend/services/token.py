from fastapi import HTTPException
from schemas.token import AccessToken, RefreshToken, Tokens
from config import settings

import jwt


def encode_jwt(payload: dict, private_key: str = settings.auth_jwt.private_key_path.read_text(), algorithm: str = settings.auth_jwt.algorithm):
    encoded_jwt = jwt.encode(payload=payload, key=private_key, algorithm=algorithm)
    return encoded_jwt

def decode_jwt(json_web_token: str, public_key: str = settings.auth_jwt.public_key_path.read_text(), algorithm: str = settings.auth_jwt.algorithm):
    decoded_jwt = jwt.decode(jwt=json_web_token, key=public_key, algorithms=algorithm)
    return decoded_jwt

def get_tokens(user_id: int) -> Tokens:
    access_token = encode_jwt(AccessToken(user_id=user_id).payload())
    refresh_token = encode_jwt(RefreshToken(user_id=user_id).payload())
    return Tokens(access_token=access_token, refresh_token=refresh_token)


def refresh_tokens(refresh_token: str):
    user_id = decode_jwt(json_web_token=refresh_token).get("user_id") if (decode_jwt(json_web_token=refresh_token).get("type") == "refresh") else None
    if user_id is None:
        raise HTTPException(status_code=400, detail="Invalid token type for refresh")
    return get_tokens(user_id)