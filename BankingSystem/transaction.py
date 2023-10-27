from abc import ABC, abstractmethod
from validators import positive_number_checker

class Transaction(ABC):
    @abstractmethod
    def execute(self):
        ...

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        ...

    @abstractmethod
    def withdraw(self, amount):
        ...

    @abstractmethod
    def add_transaction(self, transaction):
        ...

class DepositTransaction(Transaction):
    @positive_number_checker('Amount', 2)
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        self.transaction_type = "Deposit"

    def execute(self):
        self.account.deposit(self.amount)
        self.account.add_transaction(self)

class WithdrawTransaction(Transaction):
    @positive_number_checker('Amount', 2)
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        self.transaction_type = "Withdrawal"

    def execute(self):
        if self.account.balance < self.amount:
            raise ValueError("Insufficient funds")
        self.account.withdraw(self.amount)
        self.account.add_transaction(self)

class TransferTransaction(Transaction):
    def __init__(self, from_account, to_account, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0 for a transfer transaction.")
        if from_account == to_account:
            raise ValueError("From and To accounts must be different for a transfer transaction.")
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.transaction_type = "Transfer"

    def execute(self):
        if self.from_account.balance < self.amount:
            raise ValueError("Insufficient funds")
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        self.from_account.add_transaction(self)
        self.to_account.add_transaction(self)


