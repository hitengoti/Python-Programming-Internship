# Name: Goti Hiten Khodidasbhai
# Task 2 : Expense Tracker (Command-Line Application)

import csv

# 1. Add Expense - Take input & save to CSV file.
def add_expense():
    desc = input("Enter Expense Description: ")
    amount = float(input("Enter Amount(₹): "))
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])
    print(f"Expense '{desc}' of ₹{amount} added successfully.")


# 2. View Expenses - Read and display all expenses from CSV.
def view_expenses():
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        if not rows:
            print("No expenses found.")
            return
        print("\n---- All Expenses ----")
        for row in rows:
            print(f"Item: {row[0]}, Amount: ₹{row[1]}")
    except FileNotFoundError:
        print("No expenses found. Add some first.")


# 3. Total Expenses - Calculate and display total spent.
def total_expenses():
    total = 0
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                total += float(row[1])
        print(f"Total Expenses: ₹{total}")
    except FileNotFoundError:
        print("No expenses found. Add some first.")

# 4. Menu - CLI Loop for user interaction.
def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses(Items and Amounts)")
        print("3. View Total Expenses")
        print("4. Exit")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Exiting Expense Tracker")
            break
        else:
            print("Invalid Choice. Please Try Again.")

menu()