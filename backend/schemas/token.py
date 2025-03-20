from datetime import datetime, timedelta, timezone
from pydantic import BaseModel

class Tokens(BaseModel):
    access_token: str
    refresh_token: str

class Payload(BaseModel):
    user_id: int
    type: str
    iat: datetime
    exp: datetime

class AccessToken(Payload):
    iat: datetime = datetime.now(timezone.utc)
    exp: datetime = datetime.now(timezone.utc) + timedelta(minutes=15)
    type: str = "access"
    def payload(self):
        return {
            "user_id": self.user_id,
            "type": self.type,
            "iat": self.iat,
            "exp": self.exp
            }
    
class RefreshToken(Payload):
    iat: datetime = datetime.now(timezone.utc)
    exp: datetime = datetime.now(timezone.utc) + timedelta(weeks=8)
    type: str = "refresh"
    def payload(self):
        return {
            "user_id": self.user_id,
            "type": self.type,
            "iat": self.iat,
            "exp": self.exp
            }