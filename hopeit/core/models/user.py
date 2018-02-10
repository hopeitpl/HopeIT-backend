import sqlalchemy as sq
from sqlalchemy.orm import relationship

from hopeit.core.database import Base
from hopeit.core.models import Goal


class User(Base):
    __tablename__ = 'user'

    id = sq.Column(sq.Integer, primary_key=True)
    username = sq.Column(sq.String)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    device = sq.Column(sq.String)

    goals = relationship("Goal", back_populates="user", lazy='dynamic')
    payments = relationship("Payment", back_populates="user", lazy='dynamic')
    messages = relationship("Message", back_populates="user")

    def __repr__(self):
        return f'<User id={self.id} username={self.username}>'

    def to_dict(self):
        return {'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'username': self.username,
                'device': self.device,
                'total_amount': self.total_payments,
                'finished_goals': self.goals.filter(
                    Goal.finished.is_(True)).count(),
                'total_payments': self.payments.count()
                }

    @property
    def total_payments(self):
        return sum(p.operation_amount for p in self.payments)
