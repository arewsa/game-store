from sqlalchemy import select
from models.product import ProductORM
from schemas.product import CreateProduct
from sqlalchemy.ext.asyncio import AsyncSession



class ProductService:
    async def add_product(self, product: CreateProduct, session: AsyncSession) -> ProductORM:
        product_orm = ProductORM(**product.model_dump())
        session.add(product_orm)
        await session.commit()
        await session.refresh(product_orm)
        return product_orm

    async def get_all_products(self, session: AsyncSession, product_name: str | None = None) -> list[ProductORM]:
        if product_name is None:
            stmt = select(ProductORM)
        else:
            stmt = select(ProductORM).where(ProductORM.product == product_name)
        res = await session.execute(stmt)
        return list(res.scalars().all())
