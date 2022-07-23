from colorama import Fore, Style
from board.Board import Board
from players.Player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
    
    def play(self, board: Board):

        ask_position = True
        while(ask_position):
            line = input("Please insert a line:\n")
            col = input("Please insert a col:\n")

            if (board.is_valid_position(line, col)):
                ask_position = False
            else:
                self.invalid_option()
                print(board)
                print(self)

        board.set_position(self.get_symbol(), int(line), int(col))
        print(board)
        

    def __str__(self) -> str:
        return "Player"+super().__str__()