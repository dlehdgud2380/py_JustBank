import sqlite3
import account

customer_db = sqlite3.connect("customer.db")
cursor = customer_db.cursor()
cursor.execute("SELECT * FROM customer")
db_datacheck = cursor.fechall()

if db_datacheck is None:
    cursor.execute("CREATE TABLE customerdb(Name text, PhoneNumber text, Address text, Installment_saving int, Deposit int, Free_withdrawals int)")
else:
    pass

    def adduser_db(db_name, db_phoneNumber, db_address):
        customer_db = sqlite3.connect("customer.db")
        cursor = customer_db.cursor()
        list_inputdata = ('%s', '%s', '%s', '', '', '' %db_name %db_phoneNumber %db_address)
        customer_db.commit()
        customer_db.close()

    def addservice_db(db_installmentsaving, db_deposit, db_freewithdrawals):
        customer_db = sqlite3.connect("customer_db")
        cursor = customer_db.cursor()
        list_inputdata = ('', '', '', '%d', '%d', '%d' %db_installmentsaving %db_deposit %db_freewithdrawals)
        customer_db.commit()
        customer_db.close()

    def search_db(search1, search2, search3):
        search_target = [(search1, search2, search3)]
        customer_db = sqlite3.connect("customer.db")
        cursor = customer_db.cursor()
        cursor.execute("SELECT * FROM customer")
        getlist = cursor.fetchall()

        if getlist in search_target:
            print("User Found")

        else: 
            print("User Not Found")
            
                                            