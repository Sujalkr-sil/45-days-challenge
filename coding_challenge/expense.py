class ExpenseTracker:
    def __init__(self):
        self.expenses = {"Food": [], "Transport": [], "Entertainment": [], "Other": []}

    def add_expense(self, amount, category):
        if category in self.expenses:
            self.expenses[category].append(amount)
        else:
            print(f"Category '{category}' not recognized. Adding to 'Other'.")
            self.expenses["Other"].append(amount)

    def display_expenses(self):
        print("\nExpense Summary:")
        for category, amounts in self.expenses.items():
            total = sum(amounts)
            print(f"{category}: {total:.2f} (Details: {amounts})")

    def calculate_total(self):
        total = 0
        for amounts in self.expenses.values():
            total += sum(amounts)
        return total

tracker = ExpenseTracker()
n=int(input("enter the number of items to add"))
for i in range(0,n):
    amount=int(input("enter amount: "))
    category=input("enter category: ")
    tracker.add_expense(amount,category)

tracker.display_expenses()

total_expense = tracker.calculate_total()
print(f"\nTotal Expense: {total_expense:.2f}")
