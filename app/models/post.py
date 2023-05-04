from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.auth.database import User
from app.database import Base


class PostDetails(Base):
    __tablename__ = "post_user_likes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    user_id: Mapped[int] = mapped_column(Integer)
    post_id: Mapped[int] = mapped_column(Integer)


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String(length=255), nullable=False)
    author: Mapped[str] = mapped_column(String(length=20), nullable=False)
    likes: Mapped[list["User"]] = relationship("User", secondary="PostDetails", backref="post")
