'''
This is validation Module. To validate all the inputs
- This modules is called in operations.py for taking sanitized input to perform operation.
'''

import re
from datetime import datetime

def account_ID_valid():
    '''
    - This function is used validate a Account Number. It ask the user for correct account in a while loop until and unless a correct 
    format of account number is entered.
    - This function returns the int value of account number. If the account number is not an int then it raise a ValueError.
    '''
    while True:
        acc_id = input("Enter your account ID: ")
        try:
            id = int(acc_id)
        except ValueError:
            print(f"Account ID : {acc_id} must be an integer")
            continue
        
        if id < 0:
            print("ID canot be Negative")
            continue
        return int(acc_id)

def one_ID(id,bank_account):
    '''
    - This fucntion is used to return a particular account from json storage using account_no as a finder. 
    - This function return the account which was asked for. If the Account is not found it will raise an TypeError.
    '''
    for account in  bank_account:
        if account["account_no"] == id:
            return account
    else:
        raise TypeError(f"Account with ID : {id} not found!")


def phone():
    '''
    - This function is used to validate user's phone numeber in +91 standards using regular expression.
    - r"^[1-9][0-9]{9}$" : This pattern is used to format the input number.
    - This function is used in account_creation() to fill bank form.
    '''
    pattern = r"^[1-9][0-9]{9}$"
    
    while True:
        num = input("Enter your phone Number : +91 ")
        if re.match(pattern, num):
            return num
        else:
            print("Incorrect Phone number format. Try Again.")

def enter_gender():
    '''
    - This function is used to validate the user's gender based on the set of definded input : 'M','F', 'Male', 'Female'
    - This function is used in account_creation() to fill bank form.
    '''

    while True:
        gen = input("Enter your Gender[M/F] : ")
        
        if gen == 'M'or gen == 'F' or gen == 'Male' or gen == 'Female':
            return gen
        else:
            print("Enter proper gender [M/F]")

def date_of_birth():
    '''
    - This function is used to validate user's Date of birth using datetime module.
    - Then format the entered data in "%d/%m/%y"
    - This function is used in account_creation() to fill bank form.
    - Here I used try/except block to catch errors. If the dob[format] == date[format] return date -> data type is datetime.
    - except ValueError
    '''
    while True:
        dob = input("Enter your date of Birth [DD/MM/YYYY]: ")
        try:
            date = datetime.strptime(dob,"%d/%m/%Y")
            return date
        except ValueError:
            print("Invalid Date format. Please use [DD/MM/YYYY]")

def email_id():
    '''
    - This function is used to validate user's email addressu using regular expression.
    - This function is used in account_creation() to fill bank form.
    '''
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}$"
    
    while True:
        mail = input("Enter your email address : ")
        if re.match(pattern, mail):
            return mail
        else:
            print("Enter valid email address.")

def money():
    while True:
        try:
            cash = int(input("Enter the amount of money : ₹ "))
        except ValueError:
            print("Invalid input. Please enter digits only")
            continue

        if (cash > 0):
            return cash
        else:
            print("Entered Money value cannot be negative!!")
            

