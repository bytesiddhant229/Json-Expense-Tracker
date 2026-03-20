import json
from datetime import datetime

FILE = "expense.json"

print("JSON Expense Tracker")

def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def show_expenses(expenses):
    if not expenses:
        print("No expenses found.\n")
        return
    
    print("\nYour Expenses:")
    for i, exp in enumerate(expenses):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['date']}")
    print()

while True:
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. View Expenses")
    print("4. Exit")

    choice = input("Choose option: ").strip()

    expenses = load_expenses()

    if choice == "1":
        amount = float(input("Amount (₹): "))
        category = input("Category: ").strip().lower()

        entry = {
            "date": datetime.now().strftime("%d-%m-%Y"),
            "amount": amount,
            "category": category
        }

        expenses.append(entry)
        save_expenses(expenses)

        print(f"Added: ₹{amount} – {category}\n")

    elif choice == "2":
        show_expenses(expenses)

        if expenses:
            try:
                index = int(input("Enter index to delete: "))
                
                if 0 <= index < len(expenses):
                    removed = expenses.pop(index)
                    save_expenses(expenses)
                    print(f"Deleted: ₹{removed['amount']} – {removed['category']}\n")
                else:
                    print("Invalid index.\n")
            except ValueError:
                print("Enter a valid number.\n")

    elif choice == "3":
        show_expenses(expenses)

    elif choice == "4":
        print("Exiting!!")
        break

    else:
        print("Invalid choice.\n")