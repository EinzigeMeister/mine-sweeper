from helpers import Display, GameBoard


    
if __name__ == '__main__':
    display = Display()
    display.welcome_message()

    game_board = GameBoard()
    game_board.new_game('hard')