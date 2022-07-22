from pages.MultiplayerPage import MultiplayerPage
from pages.MainMenu import MainMenu
from pages.SinglePlayerPage import SinglePlayerPage
import psutil

main_menu = MainMenu(
    MultiplayerPage,
    SinglePlayerPage
)

main_menu.start()
print('RAM memory % used:', psutil.virtual_memory()[2])
