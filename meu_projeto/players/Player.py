
class Player:
    def __init__(self) -> None:
        self._name = ""
        self._symbol = ""

    def set_name(self, name) -> None:
        self._name = name

    def set_symbol(self, symbol) -> None:
        self._symbol = symbol