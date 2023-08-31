import os
from helpers import GameBoard
from models import User
class Choices:
    @classmethod
    def main_menu(cls, user):
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
    @classmethod
    def play_game(cls, user):
        os.system('clear')
        game_board = GameBoard()
        difficulty = self.choose_difficulty()
        result = game_board.new_game(difficulty)
        input("Press enter to continue")
    
    def choose_difficulty(self):
        options = ["", "easy", "medium", "hard"]
        print("Difficulty Options: ")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        difficulty_selection = input("Please select a difficulty")
        if difficulty_selection>0 and difficulty_selection<4:
            return options[difficulty_selection]
        else:
            os.system('clear')
            print("Enter a valid option")

    @classmethod
    def show_user_results(cls, user):
        print("I'm sorry this function isn't available yet")
        input("Press enter to continue")
        
    @classmethod
    def show_recent_results(self):
        print("I'm sorry this function isn't available yet")
        input("Press enter to continue")