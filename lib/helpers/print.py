from art import *

class Print:
    def welcome_message(self):
        tprint("minesweeper", font='block')

    def print_board(self, difficulty, board = {}):
    
        size = 0
        if (difficulty=='easy'):
            size = 4
        elif (difficulty=='medium'):
            size = 7
        elif (difficulty=='hard'):
            size = 9

        for n in range(size):
            pass