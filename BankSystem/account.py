import random

class Customer: 
    def customer_info(self, name, phonenumber, address):
        self.name = name
        self.phonenumber = phonenumber
        self.address = address  
    
    def new_customer(self, name, phonenumber, address):
        self.name = name
        self.phonenumber = phonenumber
        self.address = address   
        return name, phonenumber, address  

    def account(self, account_number):
        self.account_number = random.randrange(10000, 99999)
        return account_number