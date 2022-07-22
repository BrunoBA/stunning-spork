
class MultiplayerPage:
    def __init__(self, page):
        self._page = page

    def handle(self):
        print(self)
        self._page.start()
