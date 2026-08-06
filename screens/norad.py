from inputimeout import inputimeout
from rich.console import Console

from utils.generator import generate_random_code
from utils.input import get_input

console = Console()


def norad() -> None:
    print("NORAD COMMAND CENTER")
    print("FOR AUTHORIZED USERS ONLY")
    print("1. MISSILE LAUNCH SYSTEM")

    choices = ["1", "2", "exit", "quit"]
    choice = get_input(choices)

    while choice != "exit":
        if choice == "1":
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
        if choice == "2":
            # Radar view of incoming threats displaying ASCII map of USA?
            # Satellite ASCII map of Earth?
            pass

    if choice == "exit" or choice == "quit":
        return
