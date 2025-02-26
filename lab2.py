import random
class Account:

    account_count = 0 

    def __init__(self, account_number: int, account_balance: float):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_name = ""
        account_count = account_count + 1

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

    '''
    Add a function **accountConsolidate(Account acct1, Account acct2)**
    to your **Account** class that creates a new account whose balance is the sum
    of the balances in **acct1** and **acct2** and closes **acct1** and **acct2**. The new
    account should be returned. Two important rules of consolidation:
    - (a) Only accounts with the same name can be consolidated. The new
    account gets the name on the old accounts but a new account number.
    - (b) Two accounts with the same number cannot be consolidated. Otherwise, this would be an easy way to double your money!
    Check these conditions before creating the new account. If either condition
    fails, do not create the new account or close the old ones; print a useful
    message and return **None**.
    '''

    def close_account(self):
        self.account_name = self.account_name + "_CLOSED"
        self.account_balance = 0
        print(self.account_name)
        print(self.account_balance)

    def accountConsolidate(self, acct1, acct2):
        if acct1.account_name == acct2.account_name and acct1.account_number != acct2.account_number:
            new_account_number = generate_random_account_number()
            new_account = Account(new_account_number, acct1.account_balance + acct2.account_balance)
            new_account.change_name(acct1.account_name)
            acct1.close_account()
            acct2.close_account()
            return new_account
        else:
            print("Accounts cannot be consolidated.")
            return None


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

ID_prompt()

print(generate_random_account_number())