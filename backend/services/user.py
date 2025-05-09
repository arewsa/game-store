from pydantic import BaseModel
from sqlalchemy import select
from models.user import UsersORM
from sqlalchemy.ext.asyncio import AsyncSession
import bcrypt


class UserService:
    async def add(self, user: BaseModel, session: AsyncSession) -> UsersORM | None:
        user_orm = UsersORM(**user.model_dump())
        user_orm.password = bcrypt.hashpw(password=user.password.encode(), salt=bcrypt.gensalt()).decode()
        if await self.get_by_mail(user.mail, session) is None:
            session.add(user_orm)
            await session.commit()
            await session.refresh(user_orm)
            return user_orm
        return None
    
    async def get_by_id(self, user_id: int, session: AsyncSession) -> UsersORM | None:
        stmt = select(UsersORM).where(UsersORM.id == user_id)
        res = await session.execute(statement=stmt)
        return res.scalar_one_or_none()
    
    async def get_by_mail(self, mail: str, session: AsyncSession) -> UsersORM | None:
        stmt = select(UsersORM).where(UsersORM.mail == mail)
        res = await session.execute(statement=stmt)
        return res.scalar_one_or_none()