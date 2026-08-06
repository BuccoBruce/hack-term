def get_input(choices: list) -> str:
    choice = input("> ")
    while choice not in choices:
        print("Incorrect choice, please try again...")
        choice = input("> ")
    return choice
