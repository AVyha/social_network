from sqlalchemy import String, Integer, Table, Column, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


post_details = Table(
    "post_user_likes",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("user.id")),
    Column("post_id", Integer, ForeignKey("post.id"))
)


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String(length=255), nullable=False)
    author: Mapped[str] = mapped_column(String(length=20), nullable=False)
    likes = relationship("User", secondary=post_details, backref="post")
