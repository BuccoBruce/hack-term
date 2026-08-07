import json
import random

from rich.console import Console

from utils.input import get_input

console = Console(width=80)


def get_random_line(file) -> str:
    lines = open(file).read().splitlines()
    mission = random.choice(lines)

    return mission


def print_dossier() -> None:
    mission = get_random_line("data/cia/missions.txt")
    subject = get_random_line("data/cia/subjects.txt")
    status = get_random_line("data/cia/status.txt")
    last_seen = get_random_line("data/cia/locations.txt")
    classification = get_random_line("data/cia/classifications.txt")

    console.print("SUBJECT:")
    console.print(subject)
    console.print("")
    console.print("STATUS:")
    console.print(status)
    console.print("")
    console.print("LAST SEEN:")
    console.print(last_seen)
    console.print("")
    console.print("DESCRIPTION:")
    console.print(mission)
    console.print("")
    console.print("CLASSIFICATION:")
    console.print(classification)
    console.print("")


def agent_add():
    with open("data/cia/agents.json") as f:
        d = json.load(f)

    print("Input data for new agent")
    agent_id = str(input("ID: "))
    agent_name = input("Name: ")
    agency = input("Agency: ")
    alias = input("Alias: ")
    age = str(input("Age: "))
    location_city = input("City: ")
    location_country = input("Country: ")
    clearance_level = str(input("Clearance Level: "))
    cover = input("Cover Role: ")
    recruitment_date = str(input("Recruitment date (YYYY-MM-DD): "))

    data = {
        "id": agent_id,
        "subject": {"name": agent_name, "agency": agency, "alias": alias, "age": age},
        "location": {"city": location_city, "country": location_country},
        "clearance level": clearance_level,
        "cover": cover,
        "recruitment date": recruitment_date,
    }

    d["agents"].append(data)

    with open("data/cia/agents.json", "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=4)


def cia() -> None:
    print("WELCOME TO THE CENTRAL INTELLIGENCE AGENCY")
    print("CENTRALIZED COMMAND AND CONTROL")
    print("1. DOSSIER REVIEW")
    print("2. ADD NEW AGENT")
    print("3. PRINT AGENT LIST")
    choices = ["1", "2", "3", "quit", "exit"]
    choice = get_input(choices)

    while choice != "quit" or choice != "exit":
        # Agent recruit and store in json?
        # RNG Mission Generator with X% chance success minigame?
        if choice == "1":
            print_dossier()
            choice = get_input(choices)

        if choice == "2":
            agent_add()
            choice = get_input(choices)

        if choice == "3":
            with open("data/cia/agents.json") as f:
                d = json.load(f)
                for agent in d["agents"]:
                    print(f"{agent['subject']['name']}\t{agent['subject']['agency']}")
                choice = get_input(choices)

        if choice not in choices:
            print("invalid selection")
            choice = get_input(choices)

        if choice == "quit" or choice == "exit":
            return

        return
