"""
 Bank Account : Base Class ( abstraction )
"""

from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, owner, balance=0.0):
        self._owner = owner  # Encapsulation of Owner attribute
        self._balance = balance  # Encapsulation of Balance attribute

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance

    def get_owner(self):
        return self._owner

    def __str__(self):
        return f"Account owner: {self._owner} , Balance: {self._balance} "
