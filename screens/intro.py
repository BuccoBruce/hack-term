from utils.terminal import clear_screen
from screens.main_menu import main_menu
from time import sleep
def intro():
    clear_screen()
    print("#  #   #     ###  #  # ")
    print("#  #  # #   #     # #  ")
    print("####  ###  #      ##   ")
    print("#  # #   #  #     # #  ")
    print("#  # #   #   ###  #  # ")
    print("                       ")
    print("###  ##### ###    #   #")
    print(" #   #     #  #   ## ##")
    print(" #   ###   ###    # # #")
    print(" #   #     #  #   #   #")
    print(" #   ##### #   #  #   #")
    sleep(3)
    main_menu()
