from helpers import Display, Game

display = Display()
display.welcome_message()

board = {}
for n in range(4):
    for m in range(4):
        mapTuple = (n, m)
        board[mapTuple]="-"
    
