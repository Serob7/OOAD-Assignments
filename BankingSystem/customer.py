from validators import not_empty_string, email_checker

class Customer:
    @not_empty_string('Name', 1)
    @not_empty_string('Address', 2)
    @email_checker('Contact info', 3)
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_type] = account

    def get_account(self, account_type):
        return self.accounts.get(account_type)

    def get_accounts(self):
        return list(self.accounts.values())
