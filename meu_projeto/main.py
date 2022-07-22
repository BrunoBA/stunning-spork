from pages.MultiplayerPage import MultiplayerPage
from pages.MainMenu import MainMenu
from pages.SinglePlayerPage import SinglePlayerPage
from players.Player import Player
from players.Computer import Computer
import psutil

multiplayer_page = MultiplayerPage(Player(), Player())
single_player_page = SinglePlayerPage(Player(), Computer())

main_menu = MainMenu(multiplayer_page, single_player_page)

main_menu.start()
print('RAM memory % used:', psutil.virtual_memory()[2])
