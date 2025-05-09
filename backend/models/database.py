from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession, async_sessionmaker, AsyncAttrs  
from config import settings
from sqlalchemy.orm import DeclarativeBase

class DBHelper:
    def __init__(self, db_url: str):
        self.engine: AsyncEngine = create_async_engine(url=db_url)
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(bind=self.engine, expire_on_commit=False)

    def dispose(self):
        self.engine.dispose()

    async def get_session(self):
        async with self.session_factory() as session:
            yield session

    
db_helper = DBHelper(db_url=settings.database.url)

class Base(AsyncAttrs, DeclarativeBase):
    pass