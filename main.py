import json
from bank import Account
from datetime import datetime
import re

def load_data():
    try:
        with open("bank_db.json",'r') as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []

def save_data(bank_account):
    with open("bank_db.json", 'w') as file:
        json.dump(bank_account, file, indent=4)

def one_ID(id,bank_account):
    for account in  bank_account:
        if account["account_no"] == id:
            return account
    else:
        raise TypeError("Account not found!")

def account_ID_valid():
    while True:
        acc_id = input("Enter your account ID: ")
        try:
            id = int(acc_id)
        except ValueError:
            print("Account ID must be an integer")
            continue
        
        if id < 0:
            print("ID canot be Negative")
            continue
        return int(acc_id)

def account_display(info):
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
    
    print(type(info['account_no']))

def phone():
    
    pattern = r"^[1-9][0-9]{9}$"
    
    while True:
        num = input("Enter your phone Number : +91 ")
        if re.match(pattern, num):
            return num
        else:
            print("Incorrect Phone number format. Try Again.")

def enter_gender():
    while True:
        gen = input("Enter your Gender[M/F] : ")
        
        if gen == 'M'or gen == 'F' or gen == 'Male' or gen == 'Female':
            return gen
        else:
            print("Enter proper gender [M/F]")

def date_of_birth():
    while True:
        dob = input("Enter your date of Birth [DD/MM/YYYY]: ")
        try:
            date = datetime.strptime(dob,"%d/%m/%Y")
            return date
        except ValueError:
            print("Invalid Date format. Please use [DD/MM/YYYY]")

def email_id():
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}$"
    
    while True:
        mail = input("Enter your email address : ")
        if re.match(pattern, mail):
            return mail
        else:
            print("Enter valid email address.")

def account_creation(bank_account):
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
    acc_id = account_ID_valid()  
    return one_ID(acc_id,bank_account)


def deposit_money(bank_account):
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
    acc_id = int(input("Enter your account ID : "))
    
    for i in range(len(bank_account)):
        if bank_account[i]["account_no"] == acc_id:
            bank_account.pop(i)
            save_data(bank_account)
            print("Account deleted successfully")
            return 
            
    print("Account not found!")

def main():
    
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