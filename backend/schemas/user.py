from pydantic import BaseModel

class UserLoginAndPassword(BaseModel):
    login: str
    password: str
    
class User(BaseModel):
    name: str
    surname: str
    email: str

class CreateUser(User):
    password: str

class UserLoginAndId(BaseModel):
    user_id: int
    login: str

class UserInSystem(UserLoginAndId):
    password: str