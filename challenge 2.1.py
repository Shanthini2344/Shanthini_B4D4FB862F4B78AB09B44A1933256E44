class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited ${amount}. New balance: ${self._account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._account_balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def display_balance(self):
        return f"Account Balance for {self._account_holder}: ${self._account_balance}"

# Test the BankAccount class
account = BankAccount(account_number="123456789", account_holder="John Doe", initial_balance=1000.0)

print(account.display_balance())
print(account.deposit(500.0))
print(account.withdraw(200.0))
print(account.display_balance())
