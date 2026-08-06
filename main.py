import os
import sys
from time import sleep

from inputimeout import inputimeout
from rich.console import Console

console = Console()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_input(choices):
    choice = input("> ")
    while choice not in choices:
        print("Incorrect choice, please try again...")
        choice = input("> ")
    return choice


def main_screen():
    clear_screen()
    print("SELECT YOUR TARGET: ")
    print("1. NORAD MISSILE COMMAND")
    print("2. CENTRAL INTELLIGENCE AGENCY")
    print("3. DEPARTMENT OF DEFENSE")
    print("4. INTERNAL REVENUE SERVICE")

    choices = ["1", "2", "3", "4", "exit", "quit"]
    choice = get_input(choices)

    if choice == "1":
        clear_screen()
        norad_screen()
    if choice == "exit" or "quit":
        clear_screen()
        sys.exit


def norad_screen():
    print("NORAD COMMAND CENTER")
    print("FOR AUTHORIZED USERS ONLY")

    choices = ["launch missile", "exit"]
    choice = get_input(choices)

    while choice != "exit":
        if choice == "launch missile":
            console.print("MISSILE LAUNCH INITIALIZED!!!", style="bold red")
            console.print(
                "Enter cancellation code [bold red]EZ5RA[/bold red] to continue"
            )
            console.print("Missile will launch in 5 seconds")
            try:
                cancellation_code = inputimeout(prompt="> ", timeout=5)
            except:
                cancellation_code = None
            if cancellation_code == "EZ5RA":
                print("Missile Launch Aborted")
            else:
                if cancellation_code != None:
                    console.print("INVALID CANCELLATION CODE")
                else:
                    console.print("CANCELLATION TIMEOUT")
                console.print("MISSILE LAUNCHED", style="bold red")
            choice = get_input(choices)

    main_screen()


def main():
    main_screen()


main()
