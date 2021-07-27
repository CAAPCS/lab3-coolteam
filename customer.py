

class Customer:

    def __init__(self, customer_id, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.customer_id = customer_id
        self.accounts = []
    def printCustomer(self):
        print(self.first_name, self.last_name, self.address, self.customer_id)