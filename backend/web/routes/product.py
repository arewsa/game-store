from fastapi import APIRouter, Depends, Request
from schemas.product import CreateProduct, ReadProduct
from services.product import ProductService
from web.routes.dependencies import authorize, product_service
from sqlalchemy.ext.asyncio import AsyncSession
from models.database import db_helper

router = APIRouter(prefix="/products", tags=["Products"], dependencies=[Depends(authorize)])

@router.post("", status_code=201)
async def add_game(product: CreateProduct, product_service: ProductService = Depends(product_service), session: AsyncSession = Depends(db_helper.get_session)) -> ReadProduct:
    return ReadProduct.model_validate(await product_service.add_product(product, session))

@router.get("", status_code=200)
async def get_games(request: Request, product_type: str | None = None, product_service: ProductService = Depends(product_service), session: AsyncSession = Depends(db_helper.get_session)) -> list[ReadProduct]:
    list_of_products = await product_service.get_all_products(session, product_name=product_type)
    return [ReadProduct.model_validate(product) for product in list_of_products]

