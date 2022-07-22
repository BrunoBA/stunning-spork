from pages import MainMenu, MultiplayerPage, SinglePlayerPage
import psutil


main_menu = MainMenu.MainMenu(
    MultiplayerPage.MultiplayerPage,
    SinglePlayerPage.SinglePlayerPage
)

main_menu.start()
print('RAM memory % used:', psutil.virtual_memory()[2])
