import sqlalchemy as sq
from sqlalchemy.orm import relationship

from hopeit.core.database import Base


class Message(Base):
    __tablename__ = 'message'

    MESSAGE_TYPE_MESSAGE = 'message'
    MESSAGE_TYPE_PAYMENT = 'message_payment'

    id = sq.Column(sq.Integer, primary_key=True)
    message_type = sq.Column(sq.String, default=MESSAGE_TYPE_MESSAGE)
    body = sq.Column(sq.String)
    picture = sq.Column(sq.String)
    user_id = sq.Column(sq.Integer, sq.ForeignKey('user.id'))
    date = sq.Column(sq.DateTime(timezone=True), server_default=sq.func.now(),
                     nullable=False)

    user = relationship("User", back_populates="messages")

    def __repr__(self):
        return f'<Message id={self.id}>'

    def to_dict(self):
        return {'id': self.id,
                'body': self.body,
                'message_type': self.message_type,
                'picture': self.picture,
                'user_id': self.user_id,
                'date': str(self.date)}
