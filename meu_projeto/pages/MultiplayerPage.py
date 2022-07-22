
class MultiplayerPage:
    def __init__(self, player, computer):
        self._players = [player, computer]

    def handle(self):
        print(self)
        print(self._players)
        self._page.start()

    def set_next_page(self, page) -> None:
        self._page = page
