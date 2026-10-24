class Transaction:
    currency = "USD"

    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount
        self.reviewed = False

    def is_expense(self):
        return self.amount < 0

    def summary(self):
        return f"{self.date}  {self.description:<12}{self.amount:>9.2f} {self.currency}"

    def mark_reviewed(self):
        self.reviewed = True

t1 = Transaction("2026-10-01", "Coffee", -4.50)
t2 = Transaction("2026-10-02", "Salary", 3200.00)
for t in (t1, t2):
    print(t.summary(), t.is_expense())
