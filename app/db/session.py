# app/db/session.py
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from app.config import db_url

engine = create_async_engine(db_url, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db_session() -> AsyncSession:  # type: ignore
    async with async_session() as session:
        yield session
