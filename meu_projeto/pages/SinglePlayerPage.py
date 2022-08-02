from meu_projeto.board.WinnerFeedback import WinnerFeedback
from meu_projeto.pages.PlayablePage import PlayablePage


class SinglePlayerPage(PlayablePage):
    def __init__(self, player_one, computer, board):
        super().__init__(player_one, computer, board)

    def initalize_users(self):
        for index, _ in enumerate(self._players):
            current_player = self._players[index]

            if (current_player.is_computer()):
                current_player.set_name("CPU")
                continue
            
            extra_text = ''
            if len(current_player.get_name()) > 0:
                extra_text = ' Press enter to fill ({})'.format(
                    current_player.get_name()
                )
            user_name = str(
                input('Please select the user name: {}\n'.format(extra_text))
            )
            if len(user_name) > 0:
                current_player.set_name(user_name)

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
