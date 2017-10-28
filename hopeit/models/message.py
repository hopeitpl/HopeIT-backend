import sqlalchemy as sq
from sqlalchemy.orm import relationship
from sqlalchemy_imageattach.entity import Image, image_attachment

from hopeit.database import Base


class MessagePicture(Base, Image):
    __tablename__ = 'message_picture'

    message_id = sq.Column(sq.Integer, sq.ForeignKey('message.id'),
                           primary_key=True)

    message = relationship('Message', back_populates="message")

    def __repr__(self):
        return f'<MessagePicture id={self.message_id}>'


class Message(Base):
    __tablename__ = 'message'

    id = sq.Column(sq.Integer, primary_key=True)
    body = sq.Column(sq.String)
    picture = image_attachment('MessagePicture')
    user_id = sq.Column(sq.Integer, sq.ForeignKey('user.id'), nullable=True)

    user = relationship("User", back_populates="messages")

    def __repr__(self):
        return f'<Message id={self.id}>'
