"""Local expense tracker with JSON storage and CSV export."""
import csv, json
from pathlib import Path
from datetime import date

DATA = Path(__file__).with_name("expenses.json")
CATEGORIES = ("Food", "Travel", "Study", "Shopping", "Other")

def load():
    if not DATA.exists(): return []
    try:
        with DATA.open(encoding="utf-8") as f:
            result = json.load(f)
        return result if isinstance(result, list) else []
    except (OSError, json.JSONDecodeError):
        print("Saved data could not be read; starting empty.")
        return []

def save(items):
    with DATA.open("w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)

def main():
    expenses = load()
    while True:
        print("\n=== PERSONAL EXPENSE TRACKER ===")
        print("1. Add expense\n2. List expenses\n3. Summary\n4. Export CSV\n0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                amount = float(input("Amount (INR): "))
                if amount <= 0: raise ValueError
            except ValueError:
                print("Enter an amount greater than zero."); continue
            print("Categories:", ", ".join(CATEGORIES))
            category = input("Category: ").strip().title()
            if category not in CATEGORIES: category = "Other"
            note = input("Note: ").strip() or "No note"
            expenses.append({"date": date.today().isoformat(), "amount": round(amount, 2),
                             "category": category, "note": note})
            save(expenses); print("Expense saved locally.")
        elif choice == "2":
            if not expenses: print("No expenses yet.")
            for e in expenses:
                print(f"{e['date']} | INR {e['amount']:.2f} | {e['category']} | {e['note']}")
        elif choice == "3":
            if not expenses: print("No expenses yet."); continue
            print(f"Total: INR {sum(e['amount'] for e in expenses):.2f}")
            totals = {}
            for e in expenses: totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
            for category, amount in sorted(totals.items()): print(f"{category}: INR {amount:.2f}")
        elif choice == "4":
            if not expenses: print("Nothing to export."); continue
            output = DATA.with_name("expenses_export.csv")
            with output.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["date", "amount", "category", "note"])
                writer.writeheader(); writer.writerows(expenses)
            print("Exported:", output)
        elif choice == "0":
            print("Goodbye!"); break
        else: print("Invalid option.")

if __name__ == "__main__":
    main()
