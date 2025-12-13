'''
Core Engine.
Where operations are performed used in main.py
'''

import logging
import BMS_json.bank_log as bank_log
import validation as val
import BMS_json.bank as bank
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
    
    logging.info(" ==== Account Creation has Started ==== ")
    try:
        name = input("Enter your Full Name: ")
        dob = str(val.date_of_birth().date())
        gender = val.enter_gender()
        email = val.email_id()
        phone_no = val.phone()
    
        logging.info(f"Collecting data for new user")
    
        acc_creat = bank.Account(name,dob,gender,email,phone_no)
        form = acc_creat.bank_app()
        
        if form:
            bank_account.append(form)
            data.save_data(bank_account)
            
            new_id = form['account_no']
            print(f"Congratulations!! Account created succesfully ID : {new_id}")
            logging.info(f"SUCCESS!!! Account Created ID : {new_id}")
            
            dis.account_display(form)
        else:
            print("An error occured during account creation!")
            logging.error("Account not generated")
    except Exception as e:
        print("An Error occured during account creation.")
        logging.critical(f"Critical Error in account_creation : {e}", exc_info=True)

def account_info(bank_account):
    '''
    - The use of this account is simple. Fetch the information of asked account.
    - Uses account_ID_valid() and return one_ID().
    '''
    
    logging.info(" ==== Entered Account information ==== ")
    
    try:
        acc_id = val.account_ID_valid()
        info = val.one_ID(acc_id,bank_account)
        dis.account_display(info)

    # except ValueError as e:   
    #     logging.error(f"Integer input needed but User input : {id}",exc_info=True)
    #     raise e
    except TypeError as e:
        logging.warning(f"Account ID : {acc_id} not found")
        raise e
    
    return 

def deposit_money(bank_account):
    '''
    - This function is used for depositing money into the account of the user, using user's input account number.
    - Issues had been solved -> validation of account ID and account number.
    - validation of negative money deposit
    '''
    
    logging.info(" ==== Entered Desposit Money ==== ")
    
    acc_id = val.account_ID_valid()
    info = val.one_ID(acc_id,bank_account)
    deposit_cash = val.money()
    
    info['balance'] += deposit_cash
    print("Money added successfully!!")
    data.save_data(bank_account)
    logging.info("Deposit Successfull.")
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
    
    logging.info(" ==== Entered Withdraw Money ==== ")
    
    acc_id = val.account_ID_valid()
    info = val.one_ID(acc_id,bank_account)
    withdraw_cash = val.money()
    
    if info['balance'] - withdraw_cash >=0:
        info['balance'] -= withdraw_cash
        data.save_data(bank_account)
        dis.account_display(info)
        logging.info("Withdraw Successfull.")
    else:
        logging.warning("User tried to withdraw negative balance.")
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
    
    logging.info(" ==== Entered Account Deletion ==== ")
    acc_id = val.account_ID_valid()

    for idx,account  in enumerate(bank_account):
        if account['account_no'] == acc_id:
            bank_account.pop(idx)
            logging.info(f"Account ID : {acc_id} deleted successfully.")
            data.save_data(bank_account)
            print("Account deleted successfully")
            return 
    else:
        logging.warning(f"Account ID : {acc_id} not found")
        raise ValueError(f"Account ID : {acc_id} not found") 
