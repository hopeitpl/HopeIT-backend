import enum
import sqlalchemy as sq
from sqlalchemy.orm import relationship

from hopeit.database import Base


class NotificationsFreq(enum.Enum):
    week = 7
    month = 30


class Goal(Base):
    __tablename__ = 'goal'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey('user.id'))

    target = sq.Column(sq.Integer, nullable=False)
    started_at = sq.Column(
        sq.DateTime(timezone=True), server_default=sq.func.now(),
        nullable=False)
    finish_at = sq.Column(sq.DateTime(timezone=True), nullable=False)
    notify_freq = sq.Column(sq.Enum(NotificationsFreq), nullable=False)

    user = relationship("User", back_populates="goals")
