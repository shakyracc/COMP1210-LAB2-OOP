import random
class Account:

    account_count = 0 

    def __init__(self, account_number: int, account_balance: float):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_name = ""
        Account.account_count += 1

    @classmethod
    def check_account_count(cls):
        return cls.account_count

    def withdraw(self, amount):
        print("Withdrawing money")
        self.account_balance -= amount

    def deposit(self, amount):
        print("Depositing money")
        self.account_balance += amount

    def check_balance(self):
        print(f"Your balance is: {self.account_balance}")

    def charge_fee(self):
        self.account_balance = self.account_balance - 10
        return self.account_balance
    
    def change_name(self, new_name):
        self.account_name = new_name

    def close_account(self):
        if not self.account_name.endswith("_CLOSED"):
            self.account_name = self.account_name + "_CLOSED"
            self.account_balance = 0
            Account.account_count -= 1
            print("Account closed")
        else:
            print("Account already closed.")
        print(self.account_name)
        print(self.account_balance)

    def accountConsolidate(self, acct1, acct2):
        if acct1.account_name == acct2.account_name and acct1.account_number != acct2.account_number:
            new_account_number = generate_random_account_number()
            new_account = Account(new_account_number, acct1.account_balance + acct2.account_balance)
            new_account.change_name(acct1.account_name)
            acct1.close_account()
            acct2.close_account()
            print("Account consolidated!")
            return new_account
        else:
            print("Accounts cannot be consolidated.")
            return None

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
 
accounts_list = [Account(str(i), 100) for i in range(10)]

def is_valid_ID(user_id):
    for acc in accounts_list:
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
            return generate_random_account_number()
    return account_number

ID_prompt()

print(generate_random_account_number())