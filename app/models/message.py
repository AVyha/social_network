import datetime

from sqlalchemy import Column, Integer, UUID, ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    message: Mapped[str] = mapped_column(String(255))
    time = Column(DateTime, default=datetime.datetime.utcnow)

    from_user = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    to_user = Column(UUID(as_uuid=True), ForeignKey("user.id"))

    sender = relationship("User", foreign_keys=[from_user], backref="user_sender")
    receiver = relationship("User", foreign_keys=[to_user], backref="user_receiver")
