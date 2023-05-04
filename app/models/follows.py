from sqlalchemy import Integer, UUID, ForeignKey, Table, Column

from app.database import Base


follows = Table(
    "followers",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("user.id")),
    Column("follower_id", UUID(as_uuid=True), ForeignKey("user.id"))
)
