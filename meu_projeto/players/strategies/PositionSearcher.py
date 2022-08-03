from meu_projeto.board.Board import Board
from meu_projeto.board.DrawFeedback import DrawFeedback
from meu_projeto.board.WinnerFeedback import WinnerFeedback
from meu_projeto.players.strategies.Strategies import Strategies


class PositionSearcher:
    def __init__(self) -> None:
        self._strategies = Strategies()

    def find_position(
        self, board: Board, symbol: str, original_symbol: str
    ) -> tuple:    
        self._strategies.initialize_board(board, original_symbol)
        position = self._strategies.get_winner_position()
        if position is not None:
            return position

        self._strategies.initialize_board(board, board.get_next_symbol(original_symbol))
        position = self._strategies.get_winner_position()
        if position is not None:
            return position

        boardFeedback = board.check_winner()
        if (
            isinstance(boardFeedback, WinnerFeedback)
            and boardFeedback.get_symbol() == original_symbol
        ):
            return board.get_last_move()

        if isinstance(boardFeedback, DrawFeedback):
            return None

        if board.is_complete():
            return None

        copy_board = Board(board.get_matrix())
        positions = copy_board.get_positions_available()

        current_symbol = symbol
        for position in positions:
            line, col = position
            copy_board.set_position(current_symbol, line + 1, col + 1)
            current_symbol = copy_board.get_next_symbol(current_symbol)

            result = self.find_position(
                copy_board, current_symbol, original_symbol
            )
            if result is not None:
                return position

        return position
