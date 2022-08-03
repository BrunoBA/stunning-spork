from meu_projeto.board.Board import Board
from meu_projeto.players.Player import Player
from meu_projeto.players.strategies.PositionSearcher import PositionSearcher
import copy

from meu_projeto.players.strategies.Strategies import Strategies


class Computer(Player):
    def __init__(self):
        super().__init__('Computer')
        self._position_searcher = PositionSearcher()
        self._strategies = Strategies()

    def play(self, board: Board):

        # self._strategies.initialize_board(board, self.get_symbol())
        # position = self._strategies.get_winner_position()
        
        new_board = copy.deepcopy(board)
        position = self._position_searcher.find_position(
            new_board, self.get_symbol(), self.get_symbol()
        )

        (line, col) = position

        board.set_position(self.get_symbol(), line + 1, col + 1)
        board.draw()

    def is_computer(self) -> bool:
        return True

    def draw(self) -> None:
        print(self)

    def __str__(self) -> str:
        return 'Computer' + super().__str__()
