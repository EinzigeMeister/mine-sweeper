from art import *
import os
class Display:
    def welcome_message(self):
        tprint("minesweeper", font='block')

    #clears screen and prints current status of board
    def print_board(self, board = {}):
        size = board["size"]
        os.system('clear')
        print_line=" "
        for n in range(size):
            print_line+="  " + str(n)
        print(print_line)
        
        for n in range(size):
            print_line=str(n)
            for m in range(size):
                print_line+= "  "+ str(board[(n,m)])
            print(print_line)

