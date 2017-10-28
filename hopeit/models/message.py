import sqlalchemy as sq
from sqlalchemy.orm import relationship

from hopeit.database import Base


class Message(Base):
    __tablename__ = 'message'

    id = sq.Column(sq.Integer, primary_key=True)
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
                'picture': self.picture,
                'user_id': self.user_id,
                'date': str(self.date)}
