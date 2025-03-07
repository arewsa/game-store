import jwt
from databaseFunction import get_user_password
from config import Status, settings
import bcrypt

def auth_login_check(mail:str, password: str):
    try:
        user_password = get_user_password(mail)
        if user_password == Status.UserDontExistError:
            return Status.AuthError.value
        else:
            if bcrypt.checkpw(password=password.encode(), hashed_password=user_password[0].encode()):
                return Status.OK
            else:
                return Status.AuthError.value
    except Exception as _ex:
        print("[INFO] Error", _ex)

def encode_jwt(payload: dict, private_key: str = settings.auth_jwt.private_key_path.read_text(), algorithm: str = settings.auth_jwt.algorithm):
    encoded_jwt = jwt.encode(payload=payload, key=private_key, algorithm=algorithm)
    return encoded_jwt


def decode_jwt(json_web_token: str, public_key: str = settings.auth_jwt.public_key_path.read_text(), algorithm: str = settings.auth_jwt.algorithm):
    decoded_jwt = jwt.decode(jwt=json_web_token, key=public_key, algorithms=algorithm)
    return decoded_jwt