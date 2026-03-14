import json
from datetime import datetime

FILE = "expense.json"

print("JSON Expense Tracker")

while True:
    amount = float(input("Amount (₹): "))
    category = input("Category: ").strip().lower()

    entry = {
        "date": datetime.now().strftime("%d-%m-%Y"),
        "amount": amount,
        "category": category
    }

    try:
        with open(FILE, "r") as f:
            expenses = json.load(f)
    except:
        expenses = []

    expenses.append(entry)

    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

    print(f"Added: ₹{amount} – {category}\n")