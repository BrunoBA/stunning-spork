
class MainMenu:

    QUESTION_TEXT = "Digite uma opção:\n1-single player\n2-two players\n3-exit\n"

    def __init__(self, one_player, two_players):
        self.one_player = one_player(self)
        self.two_players = two_players(self)

    def ask_option(self):
        option = None
        while option is None:
            option = input(self.QUESTION_TEXT)
            
            if (option not in ["1", "2", "3"]):
                print("Opção errada")
                option = None
        return option
        
    def start(self):
        option = self.ask_option()
        
        if (option == "1"):
            self.one_player.handle()

        if (option == "2"):
            self.two_players.handle()

        return
