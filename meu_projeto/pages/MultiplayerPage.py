from pages.PlayablePage import PlayablePage


class MultiplayerPage(PlayablePage):
    def __init__(self, player_one, player_two, board):
        super().__init__(player_one, player_two, board)

    def handle(self):
        self.randomize_position()
        self.initalize_users()
        print(self._board)

        winner = None
        while (winner is None):
            user = self.get_current_user()
            print(user)
            user.play(self._board)
            self.next_player()

            winner = self._board.check_winner()

        winner_player = self.get_user_by_symbol(winner.get_symbol())

        self.winner_feedback()
        print(winner_player)

        self._board.initialize_matrix()
        self._page.start()
