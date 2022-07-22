from pages.MultiplayerPage import MultiplayerPage
from pages.MainMenu import MainMenu
from pages.SinglePlayerPage import SinglePlayerPage
from players.Human import Human
from players.Computer import Computer
import psutil

multiplayer_page = MultiplayerPage(Human(), Human())
single_player_page = SinglePlayerPage(Human(), Computer())

main_menu = MainMenu(multiplayer_page, single_player_page)

main_menu.start()
print('RAM memory % used:', psutil.virtual_memory()[2])
