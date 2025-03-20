from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: int
    img: str

class Game(Product):
    product_id: int | None = None
