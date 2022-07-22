class SinglePlayerPage:
    def __init__(self, player_one, player_two):
        self._players = [player_one, player_two]

    def handle(self):
        print("Hello I'm the the single player page")
        print(self._players)
        self._page.start()

    def set_next_page(self, page) -> None:
        self._page = page
