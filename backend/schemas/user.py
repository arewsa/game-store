from pydantic import BaseModel



class UserLogin(BaseModel):
    mail: str
    password: str

class CreateUser(BaseModel):
    name: str
    surname: str
    mail: str
    password: str

class User(BaseModel):
    id: int | None = None
    name: str
    surname: str
    mail: str

    class Config:
        from_attributes = True
