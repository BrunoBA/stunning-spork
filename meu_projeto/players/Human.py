from colorama import Fore, Style
from meu_projeto.board.Board import Board
from meu_projeto.players.Player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def play(self, board: Board):

        ask_position = True
        while ask_position:
            line = input('Please insert a line:\n')
            col = input('Please insert a col:\n')

            if board.is_valid_position(line, col):
                ask_position = False
            else:
                self.invalid_option()
                board.draw()
                self.draw()

        board.set_position(self.get_symbol(), int(line), int(col))
        board.draw()

    def draw(self) -> None:
        print(self)

    def __str__(self) -> str:
        return 'Player' + super().__str__()
