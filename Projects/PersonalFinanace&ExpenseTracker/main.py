from tracker import FinanceTracker
from transaction import Transaction

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number")

def main():
    tracker = FinanceTracker()

    while True:
        print("\n1. Add income")
        print("2. Add expense")
        print("3. Summary")
        print("4. Expenses by category")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            t = Transaction(
                get_float("Amount: "),
                input("Date: "),
                input("Description: ")
            )
            tracker.add_income(t)

        elif choice == "2":
            t = Transaction(
                get_float("Amount: "),
                input("Date: "),
                input("Description: "),
                input("Category: ")
            )
            tracker.add_expense(t)

        elif choice == "3":
            print("Income:", tracker.get_total_income())
            print("Expenses:", tracker.get_total_expenses())
            print("Balance:", tracker.get_balance())

        elif choice == "4":
            for k, v in tracker.expenses_by_category().items():
                print(k, ":", v)

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
