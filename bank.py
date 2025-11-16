import json
import random

class Bank:
    class Account:
        def __init__(self, name, dob, gender, phone_no, email, address):
            self.name = name
            self.dob = dob
            self.gender = gender
            self.phone_no = phone_no
            self.email = email
            self.address = address

        def create_account(self):     
            account = Bank.Account(self.name, self.dob, self.gender, self.phone_no, self.email, self.address)

            Bank_form = { 
                "Account_no" : random.randint(1,100),
                "name" : account.name ,
                "dob" : account.dob ,
                "gender" : account.gender ,
                "phone_no" : account.phone_no ,
                "email" : account.email ,
                "address" : account.address
            }

            with open('bank_details.json','a+') as file:
                json.dump(Bank_form,file,indent=4)


