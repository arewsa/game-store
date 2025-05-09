from pydantic import BaseModel

class CreateProduct(BaseModel):
    name: str
    price: float
    img: str
    product: str | None = None

class ReadProduct(BaseModel):
    name: str
    price: float
    img: str
    id: int

    class Config:
        from_attributes = True
