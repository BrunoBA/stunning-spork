
class MainMenu:

    QUESTION_TEXT = """
Digite uma opção:
1 - Player x Computer
2 - Player x Player
3 - Exit

"""

    def __init__(self, one_player, two_players):
        self.one_player = one_player
        self.two_players = two_players

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

        self.one_player.set_next_page(self)
        self.two_players.set_next_page(self)
        
        if (option == "1"):
            self.one_player.handle()

        if (option == "2"):
            self.two_players.handle()

        return
