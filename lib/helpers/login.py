from models import User
from helpers import session
class Login:
   def __init__(self):
      self.user_login()

   def user_login(self):
      user_selection = input("Please enter your username: ")
      if len(user_selection)>16: 
         print("enter a username 16 characters or less")
         self.user_login()
      elif len(user_selection)==0:
         print("No username detected, try again.")
         self.user_login()
      else:
         found_user = session.query(User).filter(User.username==user_selection).first()
         if not found_user:
            print("Creating new user: ")
            new_user_name = self.set_user_name(input("Please enter your name: "))
            self.user = User(name = new_user_name, username=user_selection)
            User.add_user(session, self.user)
         else:
            self.user = found_user
      
   def get_username(self):
      return self.user.username
   
   def set_user_name(self, name):
      if len(name)>0 and len(name) <50:
         return name
      else: return self.set_user_name(input("Please enter your name: "))