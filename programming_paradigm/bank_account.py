class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount:.1f}"

    def withdraw(self, amount):
        """Withdraw money if sufficient funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance:.1f}")
