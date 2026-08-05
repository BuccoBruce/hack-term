import rich


def target_select():
    print("SELECT YOUR TARGET: ")
    print("1. NORAD MISSILE COMMAND")
    print("2. CENTRAL INTELLIGENCE AGENCY")
    print("3. DEPARTMENT OF DEFENSE")
    print("4. INTERNAL REVENUE SERVICE")
    choice = input()
    choices = ["1", "2", "3", "4"]
    while choice not in choices:
        print("Incorrect choice, please try again...")
        choice = input()


def main():
    target_select()


main()
