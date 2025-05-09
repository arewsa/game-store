from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")


class Database(BaseModel):
    url: str = f"postgresql+asyncpg://{db_user}:{password}@{host}/{db_name}"

class AuthJWT(BaseModel):
    private_key_path: Path = Path("./certs/jwt-private.pem")
    public_key_path: Path = Path("./certs/jwt-public.pem")
    algorithm: str = "RS256"

class Settings(BaseSettings):
    auth_jwt: AuthJWT = AuthJWT()
    database: Database = Database()

settings = Settings()
