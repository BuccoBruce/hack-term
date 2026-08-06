import os
import secrets
import string

from inputimeout import inputimeout
from rich.console import Console

console = Console()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_input(choices: list) -> str:
    choice = input("> ")
    while choice not in choices:
        print("Incorrect choice, please try again...")
        choice = input("> ")
    return choice


def generate_random_code(length: int) -> str:
    generated_code = "".join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(length)
    )
    return generated_code.upper()


def main_screen() -> None:
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
    if choice == "exit" or choice == "quit":
        clear_screen()
        return


def norad_screen() -> None:
    print("NORAD COMMAND CENTER")
    print("FOR AUTHORIZED USERS ONLY")

    choices = ["launch missile", "exit"]
    choice = get_input(choices)

    while choice != "exit":
        if choice == "launch missile":
            random_cancellation_code = generate_random_code(5)
            console.print("MISSILE LAUNCH INITIALIZED!!!", style="bold red")
            console.print(
                f"Enter cancellation code [bold red]{random_cancellation_code}[/bold red] to continue"
            )
            console.print("Missile will launch in 5 seconds")
            try:
                cancellation_code = inputimeout(prompt="> ", timeout=5).upper()
            except:
                cancellation_code = None
            if cancellation_code == random_cancellation_code:
                print("Missile Launch Aborted")
            else:
                if cancellation_code != None:
                    console.print("INVALID CANCELLATION CODE")
                else:
                    console.print("CANCELLATION TIMEOUT")
                console.print("MISSILE LAUNCHED", style="bold red")
            choice = get_input(choices)

    main_screen()


def cia_screen() -> None:
    print("Welcome to the Central Intelligence Agency")
    print("Centralized Command and Control Center")


def main() -> None:
    main_screen()


main()
