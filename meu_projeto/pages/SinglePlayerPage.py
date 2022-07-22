class SinglePlayerPage:
    def __init__(self, page):
        self._page = page

    def start(self):
        print("Hello I'm the the single player page")
        print(self)
        self.start()