from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Game
from faker import Faker
import random

fake = Faker()

engine = create_engine('sqlite:///mine_data.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()
session.query(Game).delete()

user_list = []
for i in range(10):
    user_list.append(User(username=fake.profile('username')['username'], name=fake['en-US'].name()))
    
diff_list = ['Easy', 'Medium', 'Hard']
outcome_list = ['W', 'L']
game_list = []
for i in range(30):
   game_list.append(Game(user_username=random.choice(user_list).username, difficulty=random.choice(diff_list), outcome=random.choice(outcome_list)))

session.add_all(user_list)
session.add_all(game_list)
session.commit()
