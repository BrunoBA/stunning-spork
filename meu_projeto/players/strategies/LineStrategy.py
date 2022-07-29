from typing import Optional
from meu_projeto.board.Board import Board
from meu_projeto.players.strategies.Strategy import Strategy

class LineStrategy(Strategy):
    def __init__(self, symbol: str, board: Board) -> None:
        super().__init__(symbol, board)

    def find_position(self) -> Optional[tuple]:
        line_to_push = []
        for x in range(0, 3):
            for y in range(0, 3):
                element = self.get_element_by_position(x, y)
                line_to_push.append(element)

            pos = self.is_present("".join(line_to_push))
            if pos is not None:
                return (x, pos)
            line_to_push = []
            
        return None

            