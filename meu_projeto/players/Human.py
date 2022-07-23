from colorama import Fore, Style
from board.Board import Board
from players.Player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
    
    def play(self, board: Board):

        ask_position = True
        while (ask_position):
            line = input("Please insert line: \n")
            col = input("Please insert column: \n")
        
            ask_position = board.is_valid_position(line, col)
            print(ask_position, line, col)
            if (ask_position == False):
                self.invalid_option()
                ask_position = True

        board.set_position(self.get_symbol(), int(line), int(col))
        print(board)
        

    def __str__(self) -> str:
        return "Human"+super().__str__()