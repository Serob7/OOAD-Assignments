from validators import not_empty_string, positive_number_checker
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def add_transaction(self, transaction):
        pass

class BasicAccount(Account):
    @not_empty_string('Account type', 1)
    @positive_number_checker('Balance', 2)
    @positive_number_checker('Interest rate', 3)
    def __init__(self, account_type, balance, interest_rate):
        self.account_type = account_type
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transaction_history(self):
        return self.transactions
