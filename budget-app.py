class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"

        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount'\]:.2f}"
            items += f"{desc:<23}{amt:>7}\n"

        total = f"Total: {self.get_balance()}"
        return title + items + total


def create_spend_chart(categories):
    spent_amounts = []

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)

    percentages = []
    for spent in spent_amounts:
        percentage = int((spent / total_spent) * 100)
        percentages.append((percentage // 10) * 10)

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "

        if i != max_length - 1:
            chart += "\n"

    return chart