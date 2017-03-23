import os
import account
#import deposit
#import installment_Saving
#import Loan
import user_database


print("BankSystem 1.0 by Scoutkkun\n\n")

while True:
    print("Wellcome to JustBANK! How can i help you?\n\n")

    select_service = int(input("Select Service number! and we will help your work\n\n(1) Make new Account\n(2) Check my Account\n(3) Account Services\n(4) Loan Service\nService Number: "))
    
    if select_service == 1:
        os.system('cls' if os.name == 'nt' else 'clear')

        bankcustomer = account.Customer()
        new_bankcustomer = account.Customer()

        print("Wellcome to Account Making Service")
        print("\n")
        print("I will check your account. Fill the Answer the Question!\n")
        question_name = input("Name: ")
        question_phonenumber = int(input("Phone Number: "))
        question_address = input("Address: ")

        bankcustomer.customer_info(question_name, question_phonenumber, question_address)
        
        os.system('cls' if os.name == 'nt' else 'clear')

        user_database.search_db(bankcustomer.name, bankcustomer.phonenumber, bankcustomer.address)

        print("This Imformation already have an account with this name.")
#
#
#           print("No matches found. You can make new account!\n")
#            print("Let`s make New Account\n")
#            
#            question_name = input("Name: ")
#            question_phonenumber = int(input("Phone Number: "))
#            question_address = input("Address: ")
#
#            New_BankCustomer.new_customer(question_Name, question_phonenumber, question_address)