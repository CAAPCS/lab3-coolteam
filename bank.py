from customer import Customer
from account import Account

class Bank:

    def __init__(self):
        self.accounts = []
        self.customers = []


    def processDeposit(self, account_id, delta):
        self.accounts[account_id].balance += delta

    def processWithdraw(self, account_id, delta):
        self.accounts[account_id].balance -= delta

    def createCustomer(self, first, last, address):
        new_id = len(self.customers)
        new_customer = Customer(new_id, first, last, address)
        self.customers.append(new_customer)

    def createAccount(self, customer_id):
         new_account_id = len(self.accounts)
         new_account = Account(customer_id, new_account_id)
         self.accounts.append(new_account)
         self.customers[customer_id].accounts.append(new_account_id)
    def displayAccount(self, accounterid):
        account = self.accounts[accounterid]
        print("ACCOUNT_ID:", accounterid,"CUSTOMER_ID:",accounterid, "BALANCE:", account.balance)


    def displayCustomerAccount(self, customerid):
        customer = self.customers[customerid]
        print("CUSTOMER_ID:", customerid, "ACCOUNT_IDS:", customerid)

    def displayAllAccounts(self):
        for customer_id in range(len(self.customers)):
            self.displayCustomerAccount(customer_id)
        for account_id in range(len(self.accounts)):
            self.displayAccount(account_id)

