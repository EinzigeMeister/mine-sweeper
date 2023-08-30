import os
from helpers import GameBoard
class Choices:
    def main_menu(user = "blank"):
         os.system('clear')
         print(f'Welcome, {user}! How can I help you today?')
         print("1) View your recent games")
         print("2) View all users recent games")
         print("3) Play a new game")
         print("4) Quit")
         menu_option_selected = 0
         while menu_option_selected == 0:
            try_selected = input("Please select a valid option: ")
            if (try_selected.isnumeric() and int(try_selected)>0 and int(try_selected)<5): menu_option_selected = int(try_selected)
         return menu_option_selected
    
    def play_game(user = "blank"):
        game_board = GameBoard()
        result = game_board.new_game('easy')
        input("Press enter to continue")
    
    def show_user_results(user = "blank"):
        print("I'm sorry this function isn't available yet")
        input("Press enter to continue")
    
    def show_recent_results():
        print("I'm sorry this function isn't available yet")
        input("Press enter to continue")