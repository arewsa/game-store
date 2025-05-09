from sqlalchemy import String
from models.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class ProductORM(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128))
    price: Mapped[float] = mapped_column()
    img: Mapped[str] = mapped_column(String(128))
    product: Mapped[str] = mapped_column(String(128))
