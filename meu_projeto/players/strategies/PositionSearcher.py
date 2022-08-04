from typing import Optional
from meu_projeto.board.Board import Board
from meu_projeto.board.DrawFeedback import DrawFeedback
from meu_projeto.board.WinnerFeedback import WinnerFeedback
from meu_projeto.players.strategies.MoveNode import MoveNode
from meu_projeto.players.strategies.Strategies import Strategies
import copy


class PositionSearcher:
    def __init__(self) -> None:
        self._strategies = Strategies()

    def _default_draw_move(self, winners_positions) -> Optional[MoveNode]:
        lower_move = float('inf')
        winner_index = 0
        for index_win, winner_move in enumerate(winners_positions):
            if (
                lower_move > winner_move.get_quantity_of_moves()
                and winner_move.get_winner_symbol() == None
            ):
                lower_move = winner_move.get_quantity_of_moves()
                winner_index = index_win

        return winners_positions[winner_index]

    def _default_winner_move(
        self, winners_positions, original_symbol
    ) -> Optional[MoveNode]:
        lower_move = float('inf')
        winner_index = 0
        for index_win, winner_move in enumerate(winners_positions):
            if (
                lower_move > winner_move.get_quantity_of_moves()
                and winner_move.get_winner_symbol() == None
            ):
                lower_move = winner_move.get_quantity_of_moves()
                winner_index = index_win

        return winners_positions[winner_index]

    def find_position(
        self, board: Board, symbol: str, original_symbol: str
    ) -> MoveNode:

        self._strategies.initialize_board(board, original_symbol)
        position = self._strategies.get_winner_position()
        if position is not None:
            return MoveNode(position, symbol, original_symbol)

        self._strategies.initialize_board(
            board, board.get_next_symbol(original_symbol)
        )
        position = self._strategies.get_winner_position()
        if position is not None:
            return MoveNode(position, symbol, None)

        boardFeedback = board.check_winner()
        pos = board.get_last_move()
        if (
            isinstance(boardFeedback, WinnerFeedback)
            and boardFeedback.get_symbol() == original_symbol
        ):
            return MoveNode(pos, symbol, original_symbol)

        if isinstance(boardFeedback, DrawFeedback):
            return MoveNode(pos, symbol, None)

        if board.is_complete():
            return MoveNode(
                pos, symbol, board.get_next_symbol(original_symbol)
            )

        copied_board = copy.deepcopy(board)
        positions = copied_board.get_positions_available()

        winners_positions = []
        index_pos = 0
        current_symbol = copied_board.get_next_symbol(symbol)
        # print(copied_board)
        while index_pos < len(positions):
            position = positions[index_pos]
            line, col = position

            copied_board.set_position(current_symbol, line + 1, col + 1)

            result = self.find_position(
                copied_board, current_symbol, original_symbol
            )

            if isinstance(
                result, MoveNode
            ) and result.get_winner_symbol != board.get_next_symbol(
                original_symbol
            ):
                move_node = MoveNode((line, col), current_symbol, None)
                move_node.set_symbol(current_symbol)
                move_node.set_move(position)
                move_node.set_winner_symbol(result.get_winner_symbol())
                move_node.set_next_move(result)

                copied_board.roll_back_move()

                winners_positions.append(move_node)
                index_pos += 1

        winner_move = self._default_winner_move(
            winners_positions, original_symbol
        )
        if winner_move is not None:
            return winner_move
        return self._default_draw_move(winners_positions)
