from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base 

engine = create_engine('sqlite:///mine_data.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column('user_id', Integer(), primary_key=True)
    name = Column('user_name', String(50))
    username = Column('user_username', String())

    def __repr__(self):
        return f"<User id={self.id}, " + \
            f"name={self.name}, " + \
            f"username = {self.username}>"
    
