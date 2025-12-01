import random
class Account:
    def __init__(self,name,dob,gender,email,phone_no):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.email = email
        self.phone_no = phone_no

    def bank_app(self):
        
        form = {
            "account_no" : random.randint(1,100),
            "name" : self.name,
            "dob" : self.dob,
            "gender" : self.gender,
            "email" : self.email,
            "phone_no" : self.phone_no,
            "balance" : 0
        }
        
        return form        
