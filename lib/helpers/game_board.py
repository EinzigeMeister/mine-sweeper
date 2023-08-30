from helpers import Display
import random
display = Display()

class GameBoard:
    def new_game(self, difficulty):
        game_board = {}
        game_board['difficulty'] = difficulty
        game_board['size'] = self.setSize(difficulty)
        self.generate_board(game_board, self.add_mines(game_board))

        self.play(game_board)

    def play(self, board):
        
        user_board = dict(board)

        display.print_board(user_board)
        print("")
   
    def setSize(self, difficulty):
        if (difficulty=='easy'):
            return 4
        elif (difficulty=='medium'):
            return 6
        elif (difficulty=='hard'):
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
        pass