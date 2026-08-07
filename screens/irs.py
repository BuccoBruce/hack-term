import csv
import random

from rich.console import Console
from rich.table import Table

from utils.input import get_input

console = Console()
table = Table(title="IRS TAXPAYER DATABASE")
with open("data/irs/database.csv", newline="") as f:
    r = csv.DictReader(f)

    for column in r.fieldnames:
        table.add_column(column.upper())

    for row in r:
        print(row)
        print(row.values())
        table.add_row(*row.values())


def irs() -> None:
    print("WELCOME TO THE INTERNAL REVENUE SERVICE DATABASE")
    print("1. QUERY TAXPAYER")
    print("2. ADD TAXPAYER")
    print("3. MODIFY TAXPAYER")
    print("4. DELETE TAXPAYER")
    print("5. AUDIT RANDOM CITIZEN")
    print("6. PRINT DATABASE")
    choices = ["1", "2", "3", "4,", "5", "6", "quit", "exit"]
    choice = get_input(choices)

    while choice != "quit" or choice != "exit":
        if choice == "1":
            # Query Taxpayer
            ...
        elif choice == "2":
            # Add Taxpayer
            ...
        elif choice == "3":
            # Modify Taxpayer
            ...
        elif choice == "4":
            # Delete Taxpayer
            ...
        elif choice == "5":
            # Audit Random Citizen
            ...
        elif choice == "6":
            # Print Database
            console.print(table)
            choice = get_input(choices)

        if choice not in choices:
            print("invalid selection")
            choice = get_input(choices)

        if choice == "quit" or choice == "exit":
            return

        return
