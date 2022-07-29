from meu_projeto.board.WinnerFeedback import WinnerFeedback
from meu_projeto.pages.PlayablePage import PlayablePage


class MultiplayerPage(PlayablePage):
    def __init__(self, player_one, player_two, board):
        super().__init__(player_one, player_two, board)

    def handle(self):
        self.randomize_position()
        self.initalize_users()
        print(self._board)

        result = None
        while result is None:
            user = self.get_current_user()
            print(user)
            user.play(self._board)
            self.next_player()

            result = self._board.check_winner()

        result.draw_feedback()

        if isinstance(result, WinnerFeedback):
            winner_player = self.get_user_by_symbol(result.get_symbol())
            print(winner_player)

        self._board.initialize_matrix()
        self._page.start()
