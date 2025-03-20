from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path


host = "127.0.0.1"
db_user = "arewsa"
password = "PythonMain.Py"
db_name = "game_store"

class AuthJWT(BaseModel):
    private_key_path: Path = Path("./certs/jwt-private.pem")
    public_key_path: Path = Path("./certs/jwt-public.pem")
    algorithm: str = "RS256"

class Settings(BaseSettings):
    auth_jwt: AuthJWT = AuthJWT()

settings = Settings()
