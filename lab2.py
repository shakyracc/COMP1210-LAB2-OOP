import random
class Account:
    def __init__(self, account_number: int, account_balance: float):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_name = ""

    def withdraw(self, amount):
        print("Withdrawing money")
    
    def deposit(self, amount):
        print("Depositing money")

    def check_balance(self):
        print(f"Your balance is: {self.account_balance}")

    def charge_fee(self):
        self.account_balance = self.account_balance - 10
        return self.account_balance
    
    def change_name(self, new_name):
        self.account_name = new_name


#  Once an ID is accepted, the main menu is displayed as shown in the sample run. You can enter choice 1 for viewing the current balance, 2 for withdrawing money, 3 for depositing money, and 4 for exiting the main menu. Once you exit, the system will prompt for an id again. Thus, once the system starts, it will not stop.


def display_menu(acc):
    print(acc.account_number)
    print("Displaying the menu")
    print("Option 1: View current balance\nOption 2: Withdraw money\nOption 3: Deposit money\nOption 4: Exit main menu")
    option = input("Enter your option now")
    if option == "1":
        print("You chose option 1: View current balance")
    elif option == "2":
        print("You chose option 2: Withdraw money")
    elif option == "3":
        print("You chose option 3: Deposit money")
    elif option == "4":
        print("You chose option 4: Exit main menu\nExiting the system")
        ID_prompt()
    else: 
        print("Enter a valid option")
 
        

# Create 10 accounts in a list with ID 0, 1,...,9, and an initial balance of $100

accounts_list = [Account(str(i), 100) for i in range(10)]

#print("Print initial accounts with $100 balance:")

#for acc in accounts_list:
#    print(f"ID: {acc.account_number}, Balance: {acc.account_balance}")

# Prompt the user to enter an ID.

def is_valid_ID(user_id):
    # print(user_id)
    for acc in accounts_list:
        # print(acc.account_number)
        if acc.account_number == user_id:
            print(accounts_list[int(user_id)])
            return acc
    return False

def ID_prompt():
    while True:
        user_id = input("Please enter your ID")
        account = is_valid_ID(user_id)
        if account:
            display_menu(account)
            break
        else: 
            print("Invalid ID.")

def generate_random_account_number():
    limit = len(accounts_list)
    account_number = random.randint(limit+1, limit+50)

    for acc in accounts_list:
        if acc.account_number == account_number:
            generate_random_account_number()
    return account_number

#D_prompt()

print(generate_random_account_number())