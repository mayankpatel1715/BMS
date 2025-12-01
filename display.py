'''
This file is a UI file. used in main.py module
'''

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
