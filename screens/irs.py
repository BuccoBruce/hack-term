import csv
import random

from rich.console import Console
from rich.table import Table

from utils.input import get_input


def print_table():
    console = Console()
    table = Table(title="IRS TAXPAYER DATABASE")

    with open("data/irs/database.csv", newline="") as f:
        r = csv.reader(f)

        headers = next(r)
        for header in headers:
            table.add_column(header.upper())

        for row in r:
            table.add_row(*row)
    console.print(table)


def input_checker(valid_items):

    while item not in valid_items:
        item = input("> ")
        if item not in valid_items:
            print(f"INVALID ENTRY, MUST BE ONE OF {valid_items}")

    return item


def add_taxpayer() -> list:
    new_id = new_name = new_status = new_filing = new_year = new_balance = new_audit = (
        ""
    )

    print("ID NUMBER (IRS-XXXXX)")
    new_id = input("> ")

    print("NAME")
    new_name = input("> ")

    valid_statuses = ["ACTIVE", "DELINQUINT", "UNDER_REVIEW"]
    print("STATUS")
    new_status = get_input(valid_statuses)

    valid_filings = ["SINGLE", "JOINT"]
    print("FILING")
    new_filing = get_input(valid_filings)

    print("YEAR")
    new_year = input("> ")

    print("BALANCE")
    new_balance = input("> ")

    print("AUDIT")
    new_audit = input("> ")

    new_taxpayer = [
        new_id,
        new_name,
        new_status,
        new_filing,
        new_year,
        new_balance,
        new_audit,
    ]

    with open("data/irs/database.csv", "a", newline="") as f:
        w = csv.writer(f)
        w.writerow(new_taxpayer)


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
            add_taxpayer()
            choice = get_input(choices)
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
            print_table()
            choice = get_input(choices)

        if choice not in choices:
            print("invalid selection")
            choice = get_input(choices)

        if choice == "quit" or choice == "exit":
            return

        return
