import os
from .game_board import GameBoard
from .session import session
from sqlalchemy import create_engine
from models import Game

class Choices:
    def main_menu(self, user_logged_in):
         user = user_logged_in.user
         os.system('clear')
         print(f'Welcome, {user.username}! How can I help you today?')
         print("1) View your recent games")
         print("2) View all users recent games")
         print("3) Play a new game")
         print("4) Quit")
         menu_option_selected = 0
         while menu_option_selected == 0:
            try_selected = input("Please select a valid option: ")
            if (try_selected.isnumeric() and int(try_selected)>0 and int(try_selected)<5): menu_option_selected = int(try_selected)
         return menu_option_selected
    
    def play_game(self, user_logged_in):
        user = user_logged_in.user
        os.system('clear')
        game_board = GameBoard()
        difficulty = self.choose_difficulty()
        outcome = game_board.new_game(difficulty)
        game_record = Game(user_username=user.username, difficulty=difficulty, outcome=outcome)
        Game.add_game(session, game_record)

        input("Press enter to continue")
    
    def choose_difficulty(self):
        options = ["", "Easy", "Medium", "Hard"]
        print("Difficulty Options: ")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        difficulty_selection = input("Please select a difficulty: ")
        if difficulty_selection.isnumeric() and int(difficulty_selection)>0 and int(difficulty_selection)<4:
            return options[int(difficulty_selection)]
        else:
            os.system('clear')
            print("Enter a valid option")
            self.choose_difficulty()

    def show_user_results(self, user):
        print("I'm sorry this function isn't available yet")
        input("Press enter to continue")

    def show_recent_results(self, user):
        print("I'm sorry this function isn't available yet")
        input("Press enter to continue")