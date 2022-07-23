
from pages.PlayablePage import PlayablePage


class MultiplayerPage(PlayablePage):
    def __init__(self, player_one, player_two, board):
        super().__init__(player_one, player_two, board)

    def handle(self):
        self.randomize_position()
        self.initalize_users()

        winner = None
        while (winner is None):
            user = self.get_current_user()
            user.play(self._board)
            self.next_player()

            winner = self._board.check_winner()
        self._board.initialize_matrix()
        self._page.start()
