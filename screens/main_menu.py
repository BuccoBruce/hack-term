import sys

from screens.cia import cia
from screens.irs import irs
from screens.norad import norad
from utils.input import get_input
from utils.terminal import clear_screen


def main_menu() -> None:
    while True:
        clear_screen()
        print("SELECT YOUR TARGET: ")
        print("1. NORAD MISSILE COMMAND")
        print("2. CENTRAL INTELLIGENCE AGENCY")
        print("3. INTERNAL REVENUE SERVICE")

        choices = ["1", "2", "3", "exit", "quit"]
        choice = get_input(choices)

        if choice == "1":
            clear_screen()
            norad()

        elif choice == "2":
            clear_screen()
            cia()
        elif choice == "3":
            clear_screen()
            irs()

        if choice == "exit" or choice == "quit":
            clear_screen()
            sys.exit()
