from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  relationship

class User(Base):
    __tablename__ = 'users'

    id = Column('user_id', Integer(), primary_key=True)
    name = Column('user_name', String(50))
    username = Column('user_username', String())
    games = relationship('Game', backref='user')

    @classmethod
    def find_user_by_username(cls, session, username):
        return session.query(User).filter(User.username == username).first()
    @classmethod
    def add_user(cls, session, user):
        session.add(user)
        session.commit()

    def __repr__(self):
        return f"<User id={self.id}, " + \
            f"name={self.name}, " + \
            f"username = {self.username}>"