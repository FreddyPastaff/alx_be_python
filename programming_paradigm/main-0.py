# main.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main.py [command] [amount]")
        return

    command = sys.argv[1].lower()

    if command == "deposit" and len(sys.argv) == 3:
        try:
            amount = float(sys.argv[2])
            result = account.deposit(amount)
            print(result)
        except ValueError:
            print("Invalid deposit amount.")
    elif command == "withdraw" and len(sys.argv) == 3:
        try:
            amount = float(sys.argv[2])
            result = account.withdraw(amount)
            print(result)
        except ValueError:
            print("Invalid withdrawal amount.")
    elif command == "balance":
        print(account.get_account_balance())
    else:
        print("Invalid command or arguments.")

if __name__ == "__main__":
    main()