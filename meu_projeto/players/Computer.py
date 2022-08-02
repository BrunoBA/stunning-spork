from meu_projeto.board.Board import Board
from meu_projeto.players.Player import Player
from meu_projeto.players.strategies.PositionSearcher import PositionSearcher
import time
import copy

class Computer(Player):
    def __init__(self):
        super().__init__('Computer')
        self._position_searcher = PositionSearcher()

    def play(self, board: Board):
        temp_board = copy.copy(board)
        position = self._position_searcher.find_position(
            temp_board, self.get_symbol(), self.get_symbol()
        )

        print("Position returned from Computer play")
        print(position)

        (line, col) = position

        board.set_position(self.get_symbol(), line + 1, col + 1)
        board.draw()

    def is_computer(self) -> bool:
        return True

    def draw(self) -> None:
        print(self)

    def __str__(self) -> str:
        return 'Computer' + super().__str__()
