from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.post import post_details


class User(SQLAlchemyBaseUserTableUUID, Base):
    __table_args__ = {"extend_existing": True}

    username: Mapped[str] = mapped_column(
            String(length=20), unique=True, index=True, nullable=False
        )
    likes = relationship("Post", secondary=post_details, backref="user")
