from customer import Customer
from account import Account

class Bank:

    def __init__(self, deposit_amount, balance, withdraw_amount, account_id, customer_id):
        self.deposit_amount = deposit_amount
        self.balance = balance
        self.withdraw_amount = withdraw_amount
        self.account_id = account_id
        self.customer_id = customer_id
        pass #TODO

    def processDeposit(self, deposit_amount, balance,):
        i = int(input("Enter your account id"))
        self.deposit_amount = float(input("Enter your deposit amount"))
        account_list[i] = self.balance
        self.balance += self.deposit_amount
        print("Your new balance is", self.balance)
        pass #TODO

    def processWithdraw(self, withdraw_amount, balance):
        i = int(input("Enter your account id"))
        self.withdraw_amount = float(input("Enter your withdraw amount"))
        account_list[i] = self.balance
        self.balance += (0-self.withdraw_amount)
        print("Your new balance is", self.balance)
        pass #TODO

    def createCustomer(self):
        pass

    def createAccount(self, ):
        pass

    def displayAccount(self, accounterid):
        i = int(input("Enter your account id"))
        #ACCOUNT_ID: <> CUSTOMER_ID: <> BALANCE: <>
        pass #TODO

    def displayCustomerAccount(self, customerid):
        #CUSTOMER_ID: <> ACCOUNT_IDS: [ <>, <>]
        pass #TODO

    def displayAllAccounts(self):
        pass #TODO

