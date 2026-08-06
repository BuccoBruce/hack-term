from utils.input import get_input


def cia() -> None:
    print("WELCOME TO THE CENTRAL INTELLIGENCE AGENCY")
    print("CENTRALIZED COMMAND AND CONTROL")
    choices = ["1", "quit", "exit"]
    choice = get_input(choices)

    # Random Mission Report Generator?
    # Agent recruit and store in json?
    # RNG Mission Generator with X% chance success minigame?
    if choice == "quit" or choice == "exit":
        return
