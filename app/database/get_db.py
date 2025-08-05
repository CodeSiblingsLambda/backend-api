from app.config import DATABASE_URL
from app.utils.logger import create_logger

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator

logger = create_logger(__name__)

logger.debug("Creating async engine for getting the db")
engine = create_async_engine(DATABASE_URL, echo=False, future=True)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    logger.info("Yielding the DB session")

    async with AsyncSessionLocal() as session:
        yield session
