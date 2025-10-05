class BankAccount:
    def __init__(self, initial_balance = 0.0):
        self.account_balance = float(initial_balance)
     
# Desposit Method
def deposit(self, amount):
    self.account_balance += amount
    print(f"Deposited: ${amount}")

# Withdraw Method
def withdraw(self, amount):
    if amount > self.account_balance:
        return "Insufficient fund"
        self.account_balance -= amount
        return f"Withdrawn: ${amount:.1f}"

# Balance Inquiry: 
def display_balance(self):
    return f"Current Balance: ${self.account_balance:.1f}"

