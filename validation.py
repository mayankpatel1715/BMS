'''
This is validation Module. To validate all the inputs
- This modules is called in operations.py for taking sanitized input to perform operation.
'''
import logging
import bank_log
import re
from datetime import datetime

def account_ID_valid():
    '''
    - This function is used validate a Account Number. It ask the user for correct account in a while loop until and unless a correct 
    format of account number is entered.
    - This function returns the int value of account number. If the account number is not an int then it raise a ValueError.
    '''
    
    logging.info(" ====  Entering Account ID Validation ==== ")
    
    while True:
        acc_id = input("Enter your account ID: ")
        logging.info(f"User entering Account ID : {acc_id}")
        
        try:
            id = int(acc_id)
        except ValueError:
            print(f"Account ID : {acc_id} must be an integer")
            logging.warning(f"Input validation failed : User entered non-integeer value: {acc_id}")
            continue
        
        if id < 0:
            print("ID canot be Negative")
            logging.warning(f"User typed negative Account ID : {id}")
            continue
        
        logging.info(f"Account ID : {acc_id} validated successfully")
        return int(acc_id)

def one_ID(id,bank_account):
    '''
    - This fucntion is used to return a particular account from json storage using account_no as a finder. 
    - This function return the account which was asked for. If the Account is not found it will raise an TypeError.
    '''
    
    logging.info(" ==== Entering Account Validation ==== ")
    
    for account in  bank_account:
        if account["account_no"] == id:
            logging.info(f"User is trying to find Account ID : {id}")
            logging.info(f"Account with ID : {id} founded!!")
            return account
    else:
        raise TypeError(f"Account ID : {id} not found!!")


def phone():
    '''
    - This function is used to validate user's phone numeber in +91 standards using regular expression.
    - r"^[1-9][0-9]{9}$" : This pattern is used to format the input number.
    - This function is used in account_creation() to fill bank form.
    '''
    
    logging.info(" ==== Entered phone number validation ==== ")
    
    pattern = r"^[1-9][0-9]{9}$"
    
    while True:
        num = input("Enter your phone Number : +91 ")
        if re.match(pattern, num):
            logging.info("Phone number Verified.")
            return num
        else:
            logging.warning("Invalid phone number.")
            print("Incorrect Phone number format. Try Again.")

def enter_gender():
    '''
    - This function is used to validate the user's gender based on the set of definded input : 'M','F', 'Male', 'Female'
    - This function is used in account_creation() to fill bank form.
    '''
    
    logging.info(" ==== Entered Gender Verification ==== ")

    while True:
        gen = input("Enter your Gender[M/F] : ")
        
        if gen == 'M'or gen == 'F' or gen == 'Male' or gen == 'Female':
            logging.info("Gender Verified.")
            return gen
        else:
            logging.info("Invalid Gender")
            print("Enter proper gender [M/F]")

def date_of_birth():
    '''
    - This function is used to validate user's Date of birth using datetime module.
    - Then format the entered data in "%d/%m/%y"
    - This function is used in account_creation() to fill bank form.
    - Here I used try/except block to catch errors. If the dob[format] == date[format] return date -> data type is datetime.
    - except ValueError
    '''
    
    logging.info(" ==== Entered Date of birth verification ==== ")
    
    while True:
        dob = input("Enter your date of Birth [DD/MM/YYYY]: ")
        try:
            date = datetime.strptime(dob,"%d/%m/%Y")
            logging.info("Date of Birth Validated Successfully")
            return date
        except ValueError:
            logging.warning("Invalid Date format.")
            print("Invalid Date format. Please use [DD/MM/YYYY]")

def email_id():
    '''
    - This function is used to validate user's email addressu using regular expression.
    - This function is used in account_creation() to fill bank form.
    '''
    
    logging.info(" ==== Entered Email Id verification ==== ")
    
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}$"
    
    while True:
        mail = input("Enter your email address : ")
        if re.match(pattern, mail):
            logging.info("Email Address Verified.")
            return mail
        else:
            logging.warning("Invalid email address.")
            print("Enter valid email address.")

def money():
    
    logging.info(" ==== Entered Money validation ==== ")

    while True:
        
        cash = input("Enter the amount of money : ₹ ")
        logging.info(f"User's entered Amount : {cash}")
        
        try:
            mon = int(cash)
        except ValueError:
            print("Invalid input. Please enter digits only")
            logging.warning(f"User entered a non-integer value : {cash}")
            continue

        if (mon > 0):
            return mon
        else:
            print("Entered Money value cannot be negative!!")
            logging.warning(f"User entered negative amount to withdraw")
            

