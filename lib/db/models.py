from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine('sqlite:///mine_data.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column('user_id', Integer(), primary_key=True)
    name = Column('user_name', String(50))
    username = Column('user_username', String())
    games = relationship('Game', backref='user')

    def __repr__(self):
        return f"<User id={self.id}, " + \
            f"name={self.name}, " + \
            f"username = {self.username}>"
    
class Game(Base):
    __tablename__ = 'game'

    id = Column('game_id', Integer(), primary_key=True)
    user_username = Column('user_username', ForeignKey('users.user_username'))
    difficulty = Column('game_difficulty', String())
    outcome = Column('game_outcome', String())

    def __repr__(self):
        return f"<Game id={self.id}, " + \
            f"user={self.user_username}, " + \
            f"difficulty={self.difficulty}, " + \
            f"outcome={self.outcome}>"