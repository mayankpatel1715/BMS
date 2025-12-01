'''
Core Engine.

Where operations are performed used in main.py
'''

import validation as val
import bank
import data
import display as dis

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
    dob = str(val.date_of_birth().date())
    gender = val.enter_gender()
    email = val.email_id()
    phone_no = val.phone()
    
    acc_creat = bank.Account(name,dob,gender,email,phone_no)
    form = acc_creat.bank_app()
    
    bank_account.append(form)
    dis.account_display(form)
    data.save_data(bank_account)

def account_info(bank_account):
    '''
    - The use of this account is simple. Fetch the information of asked account.
    - Uses account_ID_valid() and return one_ID().
    '''
    acc_id = val.account_ID_valid()  
    info = val.one_ID(acc_id,bank_account)
    dis.account_display(info)
    return 

def deposit_money(bank_account):
    '''
    - This function is used for depositing money into the account of the user, using user's input account number.
    - Issues had been solved -> validation of account ID and account number.
    - validation of negative money deposit
    '''
    acc_id = val.account_ID_valid()
    deposit_cash = val.money()
    
    info = val.one_ID(acc_id,bank_account)

    info['balance'] += deposit_cash
    print("Money added successfully!!")
    data.save_data(bank_account)
    dis.account_display(info)
    return        

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
    acc_id = val.account_ID_valid()
    withdraw_cash = val.money()
    info = val.one_ID(acc_id,bank_account)
    
    if info['balance'] - withdraw_cash >=0:
        info['balance'] -= withdraw_cash
        data.save_data(bank_account)
        dis.account_display(info)
    else:
        print("Insufficient Balance")
        

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
    acc_id = val.account_ID_valid()
    
    for i in range(len(bank_account)):
        if bank_account[i]['account_no'] == acc_id:
            bank_account.pop(i)
            data.save_data(bank_account)
            print("Account deleted successfully")
            return 
            
    print("Account not found!")