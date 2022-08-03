from typing import Optional
from meu_projeto.board.Board import Board
from meu_projeto.players.strategies.ColumnStrategy import ColumnStrategy
from meu_projeto.players.strategies.LineStrategy import LineStrategy
from meu_projeto.players.strategies.MainDiagonalStrategy import (
    MainDiagonalStrategy,
)
from meu_projeto.players.strategies.SecondaryDiagonalStrategy import (
    SecondaryDiagonalStrategy,
)


class Strategies:
    def __init__(self, board=None, symbol=None) -> None:
        if board is not None and symbol is not None:
            self.initialize_board(board, symbol)

    def initialize_board(self, board: Board, symbol: str) -> None:
        self._strategies = [
            LineStrategy(symbol, board),
            ColumnStrategy(symbol, board),
            MainDiagonalStrategy(symbol, board),
            SecondaryDiagonalStrategy(symbol, board),
        ]

    def get_winner_position(self) -> Optional[tuple]:
        for strategy in self._strategies:
            position = strategy.find_position()
            if position is not None:
                return position

        return None
