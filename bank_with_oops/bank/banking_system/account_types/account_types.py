"""
Specific Account Types (Inheritance and Polymorphism)
"""
from bank_with_oops.bank.banking_system.bank_account.bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, interest_rate=0.02):
        super().__init__(owner, balance)
        self._interest_rate = interest_rate  # Encapsulation of interest_rate

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:             # amount > 0 and self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def apply_interest(self):
        self._balance += self._balance * self._interest_rate


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0.0, overdraft_limit=500):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit  # Encapsulation of overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance + self._overdraft_limit >= amount:
                self._balance -= amount
            else:
                print("Exceeded overdraft limit.")
        else:
            print("Invalid withdrawal amount.")
