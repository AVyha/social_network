from typing import AsyncGenerator

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import engine, Base

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.models.post import post_details


class User(SQLAlchemyBaseUserTableUUID, Base):
    __table_args__ = {"extend_existing": True}

    username: Mapped[str] = mapped_column(
            String(length=20), unique=True, index=True, nullable=False
        )
    likes = relationship("Post", secondary=post_details, backref="user")


engine = engine
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# async def create_db_and_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
