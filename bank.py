'''
This is a bank Form creation program.
Here Using a Class Account I created a consistent form creation. I used this in the main.py to enter the data.

- This file is imported in operations.py
'''

import data
class Account:
    def __init__(self,name,dob,gender,email,phone_no):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.email = email
        self.phone_no = phone_no

    def account_generation():
        bank_account = data.load_data()
        if len(bank_account) == 0:
            new_user = 1001
        else:
            last_account = bank_account[-1]
            last_id = last_account['account_no']
            
            new_user = last_id + 1
            
        return new_user
    def bank_app(self):
        
        form = {
            "account_no" : Account.account_generation(),
            "name" : self.name,
            "dob" : self.dob,
            "gender" : self.gender,
            "email" : self.email,
            "phone_no" : self.phone_no,
            "balance" : 0
        }
        
        return form        
