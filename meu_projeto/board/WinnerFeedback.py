from colorama import Back, Style
from meu_projeto.board.BoardFeedback import BoardFeedback

class WinnerFeedback(BoardFeedback):
    def __init__(self, symbol, positions, type):
        self._type_of_winner = type
        super().__init__(symbol, positions, "Win")

    def __str__(self) -> str:
        mother_str = super().__str__()
        
        return mother_str + "\nType: {}".format(self._type_of_winner)

    def draw_feedback(self):
        print(Back.GREEN + "             Winner            " + Style.RESET_ALL)