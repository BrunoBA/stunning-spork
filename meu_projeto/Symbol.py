from colorama import Fore, Style

class Symbol:
    def __init__(self, symbol) -> None:
        self._symbol = symbol

    def __get_symbol_icon(self):
        color = Fore.CYAN
        if (self._symbol == "X"):
            color = Fore.RED
        return color + self._symbol + Style.RESET_ALL

    def __str__(self) -> str:
        return self.__get_symbol_icon()