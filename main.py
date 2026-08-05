import rich

def get_input(choices):
    choice = input()
    while choice not in choices:
        print("Incorrect choice, please try again...")
        choice = input()
    return choice

def main_screen():
    print("SELECT YOUR TARGET: ")
    print("1. NORAD MISSILE COMMAND")
    print("2. CENTRAL INTELLIGENCE AGENCY")
    print("3. DEPARTMENT OF DEFENSE")
    print("4. INTERNAL REVENUE SERVICE")
    choices = ["1", "2", "3", "4"]
    choice = get_input(choices)
    if choice == "1":
        norad_screen()
    return choice

def norad_screen():
    print("NORAD COMMAND CENTER")
    print("FOR AUTHORIZED USERS ONLY")
    choices = ["launch missile", "exit"]
    choice = get_input(choices)
    if choice == "launch missile":
            print("MISSILE LAUNCHED")
            norad_screen()
    if choice == "exit":
        main_screen()

def main():
    main_screen()

main()
