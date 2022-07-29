import abc
from typing import Optional
from meu_projeto.board.Board import Board

class Strategy:

    _TEMP_SYMBOL = "_"

    PATTERNS = [
        " __",
        "_ _",
        "__ "
    ]

    def __init__(self, symbol:str, board:Board) -> None:
        self._symbol = symbol
        self._board = board

    def get_pattern_by_position(self, position) -> str:
        return self.PATTERNS[position].replace(self._TEMP_SYMBOL, self._symbol)

    def get_pattern(self):
        new_array = []
        for line in self.PATTERNS:
            replaced_line = line.replace(self._TEMP_SYMBOL, self._symbol)
            new_array.append(replaced_line)
        
        return new_array

    def get_element_by_position(self, x:int, y:int) -> str:
        return self._board.get_position(x, y)

    def conditional_strategy(self, x:int, y:int) -> bool:
        return True

    def is_present(self, line:str) -> Optional[int]:
        lines = self.get_pattern()
        for index, pattern in enumerate(lines):
            if(pattern == line):
                return int(index)
        return None

    @abc.abstractclassmethod
    def find_position(self) -> Optional[tuple]:
        pass
            