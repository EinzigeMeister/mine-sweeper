from .base import Base
from sqlalchemy import Column, Integer, String,  ForeignKey

class Game(Base):
    __tablename__ = 'game'

    id = Column('game_id', Integer(), primary_key=True)
    user_username = Column('user_username', ForeignKey('users.user_username'))
    difficulty = Column('game_difficulty', String())
    outcome = Column('game_outcome', String())

    @classmethod
    def add_game(cls, session, game):
        session.add(game)
        session.commit()

    def __repr__(self):
        return f"<Game id={self.id}, " + \
            f"user={self.user_username}, " + \
            f"difficulty={self.difficulty}, " + \
            f"outcome={self.outcome}>"