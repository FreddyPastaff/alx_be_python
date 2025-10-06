class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount:.1f}"

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
        else:
            self.account_balance -= amount
            return f"Withdrew: ${amount:.1f}"

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.1f}")

