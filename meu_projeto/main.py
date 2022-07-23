from board.Board import Board
from pages.PlayablePage import PlayablePage
from pages.MultiplayerPage import MultiplayerPage
from pages.MainMenu import MainMenu
from pages.SinglePlayerPage import SinglePlayerPage
from players.Human import Human
from players.Computer import Computer
import psutil

board = Board()

multiplayer_page = MultiplayerPage(Human(), Human(), board)
single_player_page = SinglePlayerPage(Human(), Computer(), board)

main_menu = MainMenu(single_player_page, multiplayer_page)

main_menu.start()
print('RAM memory % used:', psutil.virtual_memory()[2])
