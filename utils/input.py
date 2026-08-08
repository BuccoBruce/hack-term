def get_input(choices: list) -> str:
    choice = input("> ")
    while choice not in choices:
        print("Incorrect choice, valid options are:", *choices)
        choice = input("> ")
    return choice
