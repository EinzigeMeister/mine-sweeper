from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Game
from faker import Faker

fake = Faker()

engine = create_engine('sqlite:///mine_data.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()
session.query(Game).delete()

user_list = []
for i in range(10):
    user_list.append(User(username=fake.profile('username')['username'], name=fake['en-US'].name()))
    
   
session.add_all(user_list)
session.commit()
