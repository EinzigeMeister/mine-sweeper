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
         self.user = user_selection
      
   def get_user(self):
      return self.user