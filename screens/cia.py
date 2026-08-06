from utils.input import get_input


def cia() -> None:
    print("WELCOME TO THE CENTRAL INTELLIGENCE AGENCY")
    print("CENTRALIZED COMMAND AND CONTROL")
    choices = ["1", "quit", "exit"]
    choice = get_input(choices)
    if choice == "quit" or choice == "exit":
        return
