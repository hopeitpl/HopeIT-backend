import enum
import datetime

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
    finished = sq.Column(sq.Boolean, default=False)
    notify_freq = sq.Column(sq.Enum(NotificationsFreq), nullable=False)

    user = relationship("User", back_populates="goals")

    @property
    def balance(self):
        return 0

    @property
    def next_notification(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        days_since_start = (now - self.started_at).days
        freq = self.notify_freq.value
        next_day = ((days_since_start // freq) * freq) + freq

        next_date = now + datetime.timedelta(days=next_day)
        return next_date.date()
