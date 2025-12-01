'''
This is the main path way for entering the banking application for user.
This file import data.py to load as list. Operations.py to perform operations. display.py for displaying
'''


import data
import operations as ops
import display as dis

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
    bank_account = data.load_data()
    
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
                    ops.account_creation(bank_account)
                case '2':
                    info = ops.account_info(bank_account)
                    dis.account_display(info)
                case '3':
                    ops.deposit_money(bank_account)
                case '4':
                    ops.withdraw_money(bank_account)
                case '5':
                    ops.delete_account(bank_account)
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