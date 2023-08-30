from art import *
import os
class Display:
    def welcome_message(self):
        tprint("minesweeper", font='block')

    def print_board(self, difficulty, board = {}):
    
        size = Display.setSize(difficulty)
        os.system('clear')
        print_line=" "
        for n in range(size):
            print_line+="  " + str(n)
        print(print_line)
        
        for n in range(size):
            print_line=str(n)
            for m in range(size):
                print_line+= "  "+ board[(n,m)]
            print(print_line)

    @classmethod      
    def setSize(cls, difficulty):
        if (difficulty=='easy'):
            return 4
        elif (difficulty=='medium'):
            return 7
        elif (difficulty=='hard'):
            return 9