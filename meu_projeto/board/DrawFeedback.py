from meu_projeto.board.BoardFeedback import BoardFeedback


class DrawFeedback(BoardFeedback):
    def __init__(self):
        super().__init__(None, [], "Draw", "")
    
    def __str__(self) -> str:
        return """Result: {}""".format(self.result)