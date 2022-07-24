from meu_projeto.pages.PlayablePage import PlayablePage

class SinglePlayerPage(PlayablePage):
    def __init__(self, player_one, computer, board):
        super().__init__(player_one, computer, board)

    def handle(self):
        self.randomize_position()
        user = self.get_current_user()

        user.play(self._board)

    
        self._page.start()

