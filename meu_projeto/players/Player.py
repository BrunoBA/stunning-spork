
class Player:
    def __init__(self, nome="", symbol="") -> None:
        self.name = ""
        self.symbol = ""

    def set_name(self, name) -> None:
        self.name = name

    def set_symbol(self, symbol) -> None:
        self.symbol = symbol