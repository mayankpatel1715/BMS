import json
from bank import Account

def load_data():
    try:
        with open("bank_db.json",'r') as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []

def save_data():
    pass

def account_creation():
    name = input("Enter your Full Name: ")
    dob = input("Enter your date of Birth : ")
    gender = input("Enter your Gender[M/F] : ")
    email = input("Enter your email address : ")
    phone_no = int(input("Enter your phone number : +91 "))
    
    acc_creat = Account(name,dob,gender,email,phone_no)
    form = acc_creat.bank_app()
    
    print(form)
    
    with open("bank_db.json", 'a+') as file:
        json.dump(form, file, indent=4)
        
def account_info(bank_account):
    # acc_id = int(input("Enter your account ID: "))
    
    # if bank_account["account_no"] == acc_id:
    #     return bank_account[acc_id]
    # else:
    #     raise Exception("Account no found")
    pass

def main():
    
    bank_account = load_data()
    
    while True:
        print("*--*"*30)
        print("1. Create a Bank Account ")
        print("2. See your Bank Account Information ")
        print("3. Depoist Money ")
        print("4. Withdraw Money ")
        print("5. Delete Bank Account ")
        print("6. Exit App ")
        
        choice = input("Enter your Choice : ")
        # print(bank_account)
        # print(type(bank_account))
        
        # print(bank_account["account_no"])
        
        match choice:
            case '1':
                account_creation()
            case '2':
                account_info(bank_account)
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                break
            case _:
                print("Invalid Choice.")
                
if __name__ == "__main__":
    main()
            