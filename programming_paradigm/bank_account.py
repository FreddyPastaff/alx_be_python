class BankAccount:
    def __init__(self, initial_balance = 0.0):
        self.account_balance = initial_balance

# Desposit Method
def deposit(self, amount):
    self.account_balance += amount

# Withdraw Method
def withdraw(self, amount):
    if amount > self.account_balance:
        return "Insufficient fund"
    else:
        self.account_balance -= amount
        return f"Withdrawn: ${amount:.2f}"

# Balance Inquiry: 
def display_balance(self):
    return f"current balance: ${self.account_balance:.2f}"

