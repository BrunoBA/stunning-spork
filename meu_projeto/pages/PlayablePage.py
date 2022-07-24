from random import randint, shuffle
from colorama import Fore, Back, Style
from board.Board import Board
from players.Player import Player



class PlayablePage:

    def __init__(self, p_one: Player, p_two: Player, board: Board):
        self._user_index = 0
        self._players = [p_one, p_two]
        self._page = None
        self._board = board

    def winner_feedback(self):
        print(Back.GREEN + "             Winner            " + Style.RESET_ALL)

    def initalize_users(self):
        for index, _ in enumerate(self._players):
            current_player = self._players[index]
            extra_text = ""
            if (len(current_player.get_name()) > 0):
                extra_text = " Press enter to fill ({})".format(current_player.get_name())
            user_name = str(input("Please select the user name: {}\n".format(extra_text)))
            if (len(user_name) > 0):
                current_player.set_name(user_name)

    def randomize_position(self) -> None:
        symbols = ["O", "X"]
        shuffle(symbols)

        for x in range(0, 2):
            self._players[x].set_symbol(symbols[x])        

        self._user_index = randint(0, 1)

    def next_player(self) -> None:
        if (self._user_index == 0):
            self._user_index = 1
            return

        if (self._user_index == 1):
            self._user_index = 0
            return
    
    def get_current_user(self) -> Player:
        return self._players[self._user_index]

    def set_next_page(self, page) -> None:
        self._page = page

    def play(self) -> None:
        while():
            player = self.get_current_user()
            board = player.play

    def get_user_by_symbol(self, symbol:str):
        for player in self._players:
            if (player.get_symbol() == symbol):
                return player

        return None