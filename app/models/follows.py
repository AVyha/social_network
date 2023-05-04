from sqlalchemy import Integer, UUID, ForeignKey, Table, Column
from sqlalchemy.orm import relationship

from app.database import Base


class Follow(Base):
    __tablename__ = "followers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    follower_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))

    user = relationship("User", foreign_keys=[user_id], backref="follows")
    follower = relationship("User", foreign_keys=[follower_id])
