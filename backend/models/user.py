from sqlalchemy import String
from models.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class UsersORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128))
    surname: Mapped[str] = mapped_column(String(128))
    mail: Mapped[str] = mapped_column(String(128), unique=True)
    password: Mapped[str] = mapped_column()
