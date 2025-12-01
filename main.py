'''
This is the main path way for entering the banking application for user.
In this file there are mant operations performed.

1 - json handling and json data structures. 
1.1 - load_data() -> This function is used to load the data from the storage which is present in json structure into the memory and load
it as a list in the memory. To perform operation on the list.
1.2 - save_data() -> This is used to save the data back into the storage using 'w' mode of file operation. It rewrite the entire list of json
with the current list in the memory. The data is not lost as when creating a new data and appending it to the json file we used .append to 
just add the new data to the current list. In visual: A truck have a set of data. Then you have the same set of data in warehouse. Then what
you do is jsut add one more data to the warehouse then you destroy the previous data on the truck and load the truck with current set of data from warehouse.
'''

import json
from bank import Account
from datetime import datetime
import re

def load_data():
    '''
    Loads the data as a list from json structure present the storage to memory.
    '''
    try:
        with open("bank_db.json",'r') as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []

def save_data(bank_account):
    '''
    Save the data in 'w': write mode in storage
    '''
    with open("bank_db.json", 'w') as file:
        json.dump(bank_account, file, indent=4)

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

def account_display(info):
    '''
    - This function prints an account information in a good visual manner. It takes the parameters of the particular account and prints 
    them using f-string format
    - This function is used in main() -> case 2. where the account information is stored in a variable and passed on to this function.
    '''
    print("----"*15)
    print("\n")
    print(f"Account Number : {info['account_no']}")
    print(f"Name : {info['name']}")
    print(f"Date of Birth : {info['dob']}")
    print(f"Gender : {info['gender']}")
    print(f"Email : {info['email']}")
    print(f"Phone Number : {info['phone_no']}")
    print(f"Balance : {info['balance']}")
    print("\n")
    print("----"*15)
    print("\n")

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

def account_creation(bank_account):
    '''
    - This function is used to create account.
    - This function is called from main.py -> Case '1'
    - This is the fucntion which calls the bank.py -> Class Account
    - acc_creat -> stores the values : Account(name,dob,gender,email,phone_no) which We have validated in above functions.
    - Then that values are passed to function inside the Class called bank_app() using acc_creat.bank_app() and store the return value of 
    form in bank_app() in form.
    - Then data is appended in the bank_account list using bank_account.append(form).
    - Then the said created account is displayed using account_display() function.
    - In the end, the data is saved and passed to save_data(), which save the data in storage.
    '''
    name = input("Enter your Full Name: ")
    dob = str(date_of_birth())
    gender = enter_gender()
    email = email_id()
    phone_no = phone()
    
    acc_creat = Account(name,dob,gender,email,phone_no)
    form = acc_creat.bank_app()
    
    bank_account.append(form)
    account_display(form)
    save_data(bank_account)

def account_info(bank_account):
    '''
    - The use of this account is simple. Fetch the information of asked account.
    - Uses account_ID_valid() and return one_ID().
    '''
    acc_id = account_ID_valid()  
    return one_ID(acc_id,bank_account)


def deposit_money(bank_account):
    '''
    - This function is used for depositing money into the account of the user, using user's input account number.
    ----XXXXXX-----
    Issues to solve:
    - Integerate account validation [account_ID_valid()] for account numebr validation
    - Integrate account searching [One_ID()]
    - Validation money deposit : "MONEY CAN'T BE IN NEGATIVE". 
    - Money Deposit success message. 
    - Current status of account display.  
    '''
    acc_id = int(input("Enter your account ID : "))
    money = int(input("Enter the amount of money you want to deposit : ₹ "))
    
    for account in bank_account:
        if account["account_no"] == acc_id:
            account["balance"] += money
            account_display(account)
            save_data(bank_account)
            return
        
    print("   Account not found!  ")

def withdraw_money(bank_account):
    '''
    - This function is used for withdrawing money from the user's account number using user's account number.
    - This function is called in main() -> case 4. 
    ----XXXXXX-----
    Issues to solve:
    - Integerate account validation [account_ID_valid()] for account numebr validation
    - Integrate account searching [One_ID()]
    - Validation money withdraw : "MONEY CAN'T BE IN NEGATIVE". "BALANCE CAN'T BE NEGATIVE. CHECK THE BALANCE STATUS."
    - Money Withdraw success message. 
    - Current status of account display. 
    '''
    acc_id = int(input("Enter your account ID : "))
    money = int(input("Enter the amount of money you want to withdraw : ₹ "))
    
    for account in bank_account:
        if account["account_no"] == acc_id:
            account["balance"] -= money
            account_display(account)
            save_data(bank_account)
            return
    print("   Account not found!  ")

def delete_account(bank_account):
    '''
    - This fucntion is used to delete account by using account number and list index.
    - Explaination :
    - Looping with variable i in the range of the length of the data_list.
    - If the length is 10 -> it will loop in range(10). ***Check for last account.
    - using if: bank_data[i] of that index and ['account_no'] of that index == User Entered account number.
    - Then using list method : .pop(i), we will remove the data of that index. Then return with None Value with message account deleted successfully.
    ----XXXXXX-----
    Issues to solve:
    - What if account is not present. 
    '''
    acc_id = int(input("Enter your account ID : "))
    
    for i in range(len(bank_account)):
        if bank_account[i]['account_no'] == acc_id:
            bank_account.pop(i)
            save_data(bank_account)
            print("Account deleted successfully")
            return 
            
    print("Account not found!")

def main():
    '''
    Central Brain of the program from where all the functions and features work.
    - Here, Json data from the storage is loaded in the memory using variable bank_account. From here We used the varibale everywhere.
    - Uses While loop to run endlessly.
    - Using 'match' to map the choices.
    - uses try/except to catch the errors and print them gracfully. Instead, stopping the whole program.
    - The try/except is within while loop and this doesn't break the loop if an error occured. The program continues.
    - The program only ends with we select Case '6'. 
    - The invalid message will bw printed if we select anyother message rather then -> 1,2,3,4,5,6
    '''
    bank_account = load_data()
    
    while True:
        print("*--*"*30)
        print("\n")
        print("1. Create a Bank Account ")
        print("2. See your Bank Account Information ")
        print("3. Depsit Money ")
        print("4. Withdraw Money ")
        print("5. Delete Bank Account ")
        print("6. Exit App ")
        
        choice = input("Enter your Choice : ")

        try: 
            match choice:
                case '1':
                    account_creation(bank_account)
                case '2':
                    info = account_info(bank_account)
                    account_display(info)
                case '3':
                    deposit_money(bank_account)
                case '4':
                    withdraw_money(bank_account)
                case '5':
                    delete_account(bank_account)
                case '6':
                    break
                case _:
                    print("Invalid Choice.")
        
        except TypeError as e:
            print(str(e))
            
        except ValueError as e:
            print(str(e))
            
        except Exception as e:
            print(str(e))
                
if __name__ == "__main__":
    main()