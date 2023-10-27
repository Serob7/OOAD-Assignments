from account import BasicAccount
from customer import Customer
from transaction import DepositTransaction, WithdrawTransaction, TransferTransaction

def main():
    #create Customer and Account instances
    customer = Customer("Serob", 'Yerevan', "serob@email.com")
    account1 = BasicAccount('Checking', 1000, 2.5)
    account2 = BasicAccount("Savings", 2000, 2.5)

    #adding account
    customer.add_account(account1)
    customer.add_account(account2)

    #transactions
    deposit = DepositTransaction(account1, 500)
    deposit.execute()

    withdraw = WithdrawTransaction(account2, 1500)
    withdraw.execute()

    transfer = TransferTransaction(account1, account2, 200)
    transfer.execute()

    for account in customer.get_accounts():
        print(f"Account Type: {account.account_type}, Balance: {account.balance}, Transactions: {len(account.get_transaction_history())}")

if __name__ == '__main__':
    main()

