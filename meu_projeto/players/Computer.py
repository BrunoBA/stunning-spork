from meu_projeto.board.Board import Board
from meu_projeto.players.Player import Player


class Computer(Player):
    def __init__(self):
        super().__init__('Computer')

    def play(board: Board):
        pass

    def __str__(self) -> str:
        return 'Computer' + super().__str__()
