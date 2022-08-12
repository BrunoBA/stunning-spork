from typing import Optional


class MoveNode:
    def __init__(
        self, move: tuple, symbol: str, winner_symbol: str = None
    ) -> None:
        self._move = move
        self._next_move = None
        self._symbol = symbol
        self._winner_symbol = winner_symbol

    def get_quantity_of_moves(self) -> int:
        moves = 0
        next_move = self._next_move
        while next_move is not None:
            moves = moves + 1
            next_move = next_move.get_next_node()

        return moves

    def set_move(self, move) -> None:
        self._move = move

    def set_next_move(self, next_move) -> None:
        self._next_move = next_move

    def set_symbol(self, symbol) -> None:
        self._symbol = symbol

    def set_winner_symbol(self, symbol) -> None:
        self._winner_symbol = symbol

    def get_winner_symbol(self) -> Optional[str]:
        return self._winner_symbol

    def get_move(self) -> Optional[tuple]:
        return self._move

    def get_next_node(self):
        return self._next_move

    def add_move(self, NextMoveNode, symbol: str) -> None:
        self._next_move = NextMoveNode
        self._winner_symbol = symbol

    def __str__(self) -> str:
        return """{3}
        Move = {0}
        Symbol = {1}
        Winner Symbol = {2}
        Steps to Win = {4}
        """.format(
            self._move,
            self._symbol,
            self._winner_symbol,
            str(self._next_move),
            self.get_quantity_of_moves(),
        )
