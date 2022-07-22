class SinglePlayerPage:
    def __init__(self, page):
        self._page = page

    def handle(self):
        print("Hello I'm the the single player page")
        print(self)
        self._page.start()