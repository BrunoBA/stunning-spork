from colorama import Fore, Back, Style
import abc

from board.Board import Board


class Player:
    def __init__(self, nome="", symbol="") -> None:
        self.name = ""
        self.symbol = ""

    def set_name(self, name) -> None:
        self.name = name

    def set_symbol(self, symbol) -> None:
        self.symbol = symbol

    def get_symbol(self) -> str:
        return self.symbol

    def get_name(self) -> str:
        return self.name

    @abc.abstractmethod
    def play(self, board: Board):
        return

    def invalid_option(self, text=""):
        print(Fore.RED + "Invalid option! Try again" + Style.RESET_ALL)
        if (len(text) > 0):
            print(Back.RED + text + Style.RESET_ALL)

    def __str__(self) -> str:
        return """
Name: {}
Symbol: {}
""".format(self.name, self.symbol)