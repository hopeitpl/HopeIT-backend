import sqlalchemy as sq
from sqlalchemy.orm import relationship

from hopeit.database import Base


class Payment(Base):
    __tablename__ = 'payment'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey('user.id'))
    goal_id = sq.Column(sq.Integer, sq.ForeignKey('goal.id'),  nullable=True)

    operation_number = sq.Column(sq.String)
    operation_type = sq.Column(sq.String)
    operation_status = sq.Column(sq.String)
    operation_amount = sq.Column(sq.Float, nullable=False)
    operation_currency = sq.Column(sq.String)
    operation_datetime = sq.Column(
        sq.DateTime(timezone=True), server_default=sq.func.now(),
        nullable=False)
    description = sq.Column(sq.String)
    email = sq.Column(sq.String)
    channel = sq.Column(sq.Integer, nullable=False)
    signature = sq.Column(sq.String)

    user = relationship("User", back_populates="payments")
    goal = relationship("Goal", back_populates="payments")
