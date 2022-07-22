 
class MainMenu:
    def __init__(self, single_player_page, two_players_page):
        self._single_player_page = single_player_page
        self._two_players_page = two_players_page

    def start(self) -> None:
        option = None
        while option is None:
            option = input("Digite uma opção:\n1-single player\n2-two players\n3-exit")
            
            if (option not in ["1", "2", "3"]):
                print("Opção errada")
                option = None
        
        if (option == "1"):
            self._single_player_page.start(self)
            return
        if (option == "2"):
            self._two_players_page.start(self)
            return

        return
