from transaction import Transaction
from file_manager import FileManager

class FinanceTracker:
    def __init__(self):
        self.file_manager = FileManager()
        self.income = []
        self.expenses = []
        self.load()

    def load(self):
        data = self.file_manager.load_data()
        self.income = [Transaction.from_dict(t) for t in data["income"]]
        self.expenses = [Transaction.from_dict(t) for t in data["expenses"]]

    def save(self):
        data = {
            "income": [t.to_dict() for t in self.income],
            "expenses": [t.to_dict() for t in self.expenses]
        }
        self.file_manager.save_data(data)

    def add_income(self, transaction):
        self.income.append(transaction)
        self.save()

    def add_expense(self, transaction):
        self.expenses.append(transaction)
        self.save()

    def get_total_income(self):
        return sum(t.amount for t in self.income)

    def get_total_expenses(self):
        return sum(t.amount for t in self.expenses)

    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()

    def expenses_by_category(self):
        summary = {}
        for t in self.expenses:
            summary[t.category] = summary.get(t.category, 0) + t.amount
        return summary
