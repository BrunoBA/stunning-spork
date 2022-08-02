from meu_projeto.board.Board import Board
from meu_projeto.board.DrawFeedback import DrawFeedback
from meu_projeto.board.WinnerFeedback import WinnerFeedback


class PositionSearcher:
    def __init__(self) -> None:
        pass

    def find_position(
        self, board: Board, symbol: str, original_symbol: str
    ) -> tuple:

        boardFeedback = board.check_winner()
        if (
            isinstance(boardFeedback, WinnerFeedback)
            and boardFeedback.get_symbol() == original_symbol
        ):
            return board.get_last_move()

        if isinstance(boardFeedback, DrawFeedback):
            return board.get_last_move()

        if (
            isinstance(boardFeedback, WinnerFeedback)
            and boardFeedback.get_symbol() != original_symbol
        ):
            return None

        copy_board = Board(board.get_matrix())
        positions = copy_board.get_positions_available()

        for position in positions:
            line, col = position
            copy_board.set_position(symbol, line, col)
            next_symbol = copy_board.get_next_symbol(symbol)

            result = self.find_position(
                copy_board, next_symbol, original_symbol
            )
            if result is not None:
                return position

        return position
