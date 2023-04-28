from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME


class Base(DeclarativeBase):
    pass


engine = create_async_engine(f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
