from bank import Bank
import os
import json

def load_data():
    pass

def Account_creation():
    name = input("Enter your full name : ")
    dob = input("Enter your date of birth [DD/MM/YYYY] : ")
    gender = input("Enter your gender [M/F] : ")
    phone_no = int(input("Enter your phone number : +91 "))
    email = input("Enter your email address : ")
    address = input("Enter your residential address : ")
    new_acc = Bank.Account(name, dob, gender, phone_no, email,address)
    new_acc.create_account()

def main():
    while True:
        print("X-----X----"*10)
        print("  Welcome to Sandhuk  ")
        print("Choose your Options!")
        print("1. Create a New Account")
        print("2. Deposit Money")
        print("2. Withdraw Money")
        print("4. Check Account Status")
        print("5. Delete Account")
        print("6. Exit the APP")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case '1' :
                Account_creation()
            case '2' :
                pass
            case '3' :
                pass
            case '4' :
                pass
            case '5' :
                pass
            case '6' :
                break
            case _:
                print("Invalid choice")
            
if __name__ == "__main__":
    main()