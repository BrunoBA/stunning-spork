from colorama import Fore, Style
from typing import Optional

from meu_projeto.board.BoardFeedback import BoardFeedback
from meu_projeto.board.WinnerFeedback import WinnerFeedback
from meu_projeto.board.DrawFeedback import DrawFeedback


class Board:

    EMPTY_VALUE = ' '

    def __init__(self, matrix=None) -> None:
        self._moves = []
        if matrix is not None:
            self._matrix = matrix
        else:
            self.initialize_matrix()

    def get_move_by_round(self, round: int) -> tuple:
        return self._moves[round]

    def get_moves(self) -> tuple:
        return self._moves

    def roll_back_move(self) -> None:
        if len(self._moves) == 0:
            return None

        last_move = self._moves[len(self._moves) - 1]
        (line, col) = last_move
        self._matrix[line][col] = self.EMPTY_VALUE
        self._moves.pop()

    def get_last_move(self) -> Optional[tuple]:
        if len(self._moves) == 0:
            return None

        return self._moves[len(self._moves) - 1]

    def get_next_symbol(self, current_symbol: str) -> str:
        if current_symbol == 'O':
            return 'X'

        if current_symbol == 'X':
            return 'O'

    def get_positions_available(self):
        positions = []

        for x, line in enumerate(self._matrix):
            for y, el in enumerate(line):
                if el == self.EMPTY_VALUE:
                    empty_position = (x, y)
                    positions.append(empty_position)

        return positions

    def get_matrix(self):
        return self._matrix

    def get_position(self, x: int, y: int) -> str:
        return self._matrix[x][y]

    def draw(self) -> None:
        print(self)

    def is_valid_position(self, line, col) -> bool:
        if not line.isnumeric() or not col.isnumeric():
            return False

        if len(line) == 0 or len(col) == 0:
            return False

        if int(col) < 1 or int(col) > 3:
            return False

        if int(line) < 1 or int(line) > 3:
            return False

        return self._matrix[int(line) - 1][int(col) - 1] == self.EMPTY_VALUE

    def set_position(self, symbol, line, col) -> None:
        # if self.is_valid_position(line, col):
        parsed_line = line - 1
        parsed_col = col - 1
        self._moves.append((parsed_line, parsed_col))
        self._matrix[parsed_line][parsed_col] = symbol

    def set_matrix(self, matrix) -> None:
        self._matrix = matrix

    def initialize_matrix(self) -> None:
        self._matrix = []
        self._moves = []
        for _ in range(0, 3):
            self._matrix.append(
                [self.EMPTY_VALUE, self.EMPTY_VALUE, self.EMPTY_VALUE]
            )

    def get_feedback_colors(self, element) -> str:
        color = Fore.CYAN
        if element == 'X':
            color = Fore.RED
        return color

    def is_complete(self) -> bool:

        for _, line in enumerate(self._matrix):
            for el in line:
                if el == self.EMPTY_VALUE:
                    return False

        return True

    def __check__winner_line(self) -> Optional[BoardFeedback]:
        for line in range(0, 3):
            line_result = ''.join(self._matrix[line])
            if line_result == 'OOO' or line_result == 'XXX':
                positions = [(line, 0), (line, 1), (line, 2)]
                symbol = self._matrix[line][0]
                return WinnerFeedback(symbol, positions, 'Line')

        return None

    def __check__winner_col(self) -> Optional[BoardFeedback]:
        col_result = []
        for col in range(0, 3):
            col_result = ''.join(
                [
                    self._matrix[0][col],
                    self._matrix[1][col],
                    self._matrix[2][col],
                ]
            )
            if col_result == 'OOO' or col_result == 'XXX':
                positions = [(0, col), (1, col), (2, col)]
                symbol = self._matrix[0][col]
                return WinnerFeedback(symbol, positions, 'Column')

        return None

    def __check__winner_secondary_diagonal(self) -> Optional[BoardFeedback]:

        filled_diagonal = []
        positions = []
        for line_index in range(0, 3):
            for col_index in range(0, 3):
                if line_index + col_index == 2:
                    filled_diagonal.append(self._matrix[line_index][col_index])
                    positions.append((line_index, col_index))

        return self.__check_diagonal_diagonal(positions, filled_diagonal)

    def __check__winner_main_diagonal(self) -> Optional[BoardFeedback]:

        filled_diagonal = []
        positions = []
        for x in range(0, 3):
            filled_diagonal.append(self._matrix[x][x])
            positions.append((x, x))

        return self.__check_diagonal_diagonal(positions, filled_diagonal)

    def __check_diagonal_diagonal(
        self, positions, filled_diagonal
    ) -> Optional[BoardFeedback]:
        main_diagonal = ''.join(filled_diagonal)
        if main_diagonal == 'OOO' or main_diagonal == 'XXX':
            symbol = filled_diagonal[0]
            return WinnerFeedback(symbol, positions, 'Diagonal')

        return None

    def check_winner(self) -> Optional[BoardFeedback]:
        checks = [
            self.__check__winner_line(),
            self.__check__winner_col(),
            self.__check__winner_secondary_diagonal(),
            self.__check__winner_main_diagonal(),
        ]

        for check in checks:
            if check is not None:
                return check

        if self.is_complete():
            return DrawFeedback()

        return None

    def check_winner_symbol(self) -> Optional[str]:

        check = self.check_winner()
        if check is not None:
            return check.get_symbol

        return None

    def __str__(self) -> str:
        copy_matrix = []
        for _ in self._matrix:
            copy_matrix.append(
                [self.EMPTY_VALUE, self.EMPTY_VALUE, self.EMPTY_VALUE]
            )

        for index_line, line in enumerate(self._matrix):
            for index_col, col in enumerate(line):
                color = self.get_feedback_colors(col)
                el = color + col + Style.RESET_ALL
                copy_matrix[index_line][index_col] = el

        result = self.check_winner()
        if result is None:
            result = ''

        return """
        col 1   col 2   col 3
              |       |       
line 1    {}   |   {}   |   {}   
       _______|_______|_______
              |       |      
line 2    {}   |   {}   |   {}    
       _______|_______|_______  
              |       |      
line 3    {}   |   {}   |   {}    
              |       |     
        """.format(
            copy_matrix[0][0],
            copy_matrix[0][1],
            copy_matrix[0][2],
            copy_matrix[1][0],
            copy_matrix[1][1],
            copy_matrix[1][2],
            copy_matrix[2][0],
            copy_matrix[2][1],
            copy_matrix[2][2],
        )
