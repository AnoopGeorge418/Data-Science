class Transaction:
    def __init__(self, amount, date, description, category=None):
        self.amount = amount
        self.date = date
        self.description = description
        self.category = category

    def to_dict(self):
        return {
            "amount": self.amount,
            "date": self.date,
            "description": self.description,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["amount"],
            data["date"],
            data["description"],
            data.get("category")
        )
