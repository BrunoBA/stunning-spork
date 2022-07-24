import abc

class BoardFeedback:
    def __init__(self, symbol, positions, result) -> None:
        self.symbol = symbol
        self.positions = positions
        self.result = result
        self.type = type

    def get_symbol(self) -> str:
        return self.symbol

    def __str__(self) -> str:
        return """Symbol: {}
Positions: {}
Result: {}""".format(self.symbol, self.positions, self.result)

    @abc.abstractmethod
    def draw_feedback(self) -> None:
        pass