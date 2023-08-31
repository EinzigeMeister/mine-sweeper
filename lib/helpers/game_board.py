from helpers import Display
from termcolor import colored
import random
display = Display()

class GameBoard:
    game_board = {}
    user_board = {}
    result = ""
    def new_game(self, difficulty):
        self.game_board['difficulty'] = difficulty
        self.game_board['size'] = self.setSize(difficulty)
        self.generate_board(self.game_board, self.add_mines(self.game_board))
        self.user_board = dict(self.game_board)
        self.generate_board(self.user_board)
        self.play()
        return self.result

    def play(self):
        if self.result =="":
            display.print_board(self.user_board)
            x_coordinate = input("Enter a valid 'x' coordinate: ")
            y_coordinate = input("Enter a valid 'y' coordinate: ")
            if (not x_coordinate.isnumeric() or not y_coordinate.isnumeric() or int(x_coordinate)<0 or int(y_coordinate)<0 or int(x_coordinate)>=self.game_board['size'] or int(y_coordinate)>=self.game_board['size']):
                self.play()
                return
            x_int = int(x_coordinate)
            y_int = int(y_coordinate)
            self.check_location((y_int,x_int))
            self.check_win()
            if (self.result==""):
                self.play()
            elif self.result =="L":
                display.print_board(self.user_board)
                print(colored("You lose :(", "red"))
            elif self.result =="W":
                display.print_board(self.game_board)
                print(colored("You win!", "green"))

    def setSize(self, difficulty):
        if (difficulty=='Easy'):
            return 4
        elif (difficulty=='Medium'):
            return 6
        elif (difficulty=='Hard'):
            return 9
    
    def generate_board(self, board, mine_loc = []):
        for x in range(board['size']):
            for y in range(board['size']):
                mapTuple = (x, y)
                if (x*board['size']+y in mine_loc):
                    board[mapTuple] = "*"
                else:
                    board[mapTuple]="-"
        if (len(mine_loc)>0):
            self.add_numbers(board)

    def add_mines(self, board):
        difficulty = board['difficulty']
        size = board['size']
        mines=0
        if (difficulty=='easy'):
            mines=3
        elif (difficulty=='medium'):
            mines=10
        elif (difficulty=='hard'):
            mines=27
        mine_range = range(0,size*size)
        mine_loc = random.sample(mine_range, mines)
        
        return mine_loc

    def add_numbers(self, board):
        for x in range(board['size']):
            for y in range(board['size']):
                if (board[(x, y)]=='-'):
                    adjacent_mines = 0
                    if (self.can_search(x-1, y, board['size'])):
                        if board[(x-1, y)]=='*': adjacent_mines+=1
                    if (self.can_search(x-1, y-1, board['size'])):
                        if board[(x-1, y-1)]=='*': adjacent_mines+=1
                    if (self.can_search(x, y-1, board['size'])):
                        if board[(x, y-1)]=='*': adjacent_mines+=1
                    if (self.can_search(x+1, y-1, board['size'])):
                        if board[(x+1, y-1)]=='*': adjacent_mines+=1
                    if (self.can_search(x+1, y, board['size'])):
                        if board[(x+1, y)]=='*': adjacent_mines+=1
                    if (self.can_search(x+1, y+1, board['size'])):
                        if board[(x+1, y+1)]=='*': adjacent_mines+=1
                    if (self.can_search(x, y+1, board['size'])):
                        if board[(x, y+1)]=='*': adjacent_mines+=1
                    if (self.can_search(x-1, y+1, board['size'])):
                        if board[(x-1, y+1)]=='*': adjacent_mines+=1
                    board[(x,y)] = adjacent_mines

    def can_search(self, x, y, size):
        return not (x<0 or y<0 or x==size or y ==size)
    
    def check_location(self, loc):
        if not self.user_board[loc] =="-":
            return
        if self.game_board[loc]=="*":
            self.result = "L"
        self.user_board[loc]=self.game_board[loc]

    def check_win(self):
        for n in range (self.game_board['size']):
            for m in range (self.game_board['size']):
                if not (str(self.game_board[(n, m)])==str(self.user_board[(n, m)]) or (str(self.game_board[(n, m)])=='*' and str(self.user_board[(n, m)])=='-')):
                    return
        self.result = "W"