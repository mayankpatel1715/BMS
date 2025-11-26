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

def save_data(bank_account):
    with open("bank_db.json", 'w') as file:
        json.dump(bank_account, file, indent=4)

def account_creation(bank_account):
    name = input("Enter your Full Name: ")
    dob = input("Enter your date of Birth : ")
    gender = input("Enter your Gender[M/F] : ")
    email = input("Enter your email address : ")
    phone_no = int(input("Enter your phone number : +91 "))
    
    acc_creat = Account(name,dob,gender,email,phone_no)
    form = acc_creat.bank_app()
    
    bank_account.append(form)
    
    save_data(bank_account)
    
        
def account_info(bank_account):
    acc_id = int(input("Enter your account ID: "))
    
    for account in  bank_account:
        if account["account_no"] == acc_id:
            return account
    else:
        raise Exception("Account no found")

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
                account_creation(bank_account)
            case '2':
                info = account_info(bank_account)
                print(f"\n {info} \n")
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
            