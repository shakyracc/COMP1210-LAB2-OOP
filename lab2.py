import random

class Customer:
    def __init__(self, customer_name, customer_address):
        self.customer_name = customer_name
        self.customer_address = customer_address

    def __str__(self):
        return f"Customer name: {self.customer_name}, Customer address: {self.customer_address}"

class Bank: 
    def __init__(self, bank_name, bank_address):
        self.bank_name = bank_name
        self.bank_address = bank_address

    def __str__(self):
        return f"Bank name: {self.bank_name}, Bank address: {self.bank_address}"

class Account:

    account_count = 0 

    def __init__(self, account_number: str, account_balance: float, customer: Customer, bank: Bank):
        self.account_number = account_number
        self.account_balance = account_balance
        self.customer = customer
        self.bank = bank
        self.account_name = customer.customer_name
        Account.account_count += 1

    def __str__(self):
            return f"Account Number: {self.account_number}, Name: {self.account_name}, Balance: {self.account_balance:.2f}"

    @classmethod
    def check_account_count(cls):
        return cls.account_count
    
    def change_name(self, new_name):
        self.account_name = new_name

    def charge_fee(self):
        self.account_balance = self.account_balance - 10

    def check_balance(self):
        print(f"Your balance is: {self.account_balance:.2f}")

    def withdraw(self, amount):
        print("Withdrawing: $", amount)
        self.account_balance -= amount
        print(f"Your balance is: {self.account_balance:.2f}")

    def deposit(self, amount):
        print("Depositing: $", amount)
        self.account_balance += amount
        print(f"Your balance is: {self.account_balance:.2f}")

    def close_account(self):
        if not self.account_name.endswith("_CLOSED"):
            self.account_name = self.account_name + "_CLOSED"
            self.account_balance = 0
            Account.account_count -= 1
            print(f"{self}")
        else:
            print(f"Account {self.account_number} already closed.")

    @staticmethod
    def accountConsolidate(acct1, acct2):
        if acct1.account_name == acct2.account_name and acct1.account_number != acct2.account_number:
            new_account_number = generate_random_account_number()
            new_balance =  acct1.account_balance + acct2.account_balance

            new_account = Account(new_account_number, new_balance, acct1.customer, acct1.bank)

            new_account.change_name(acct1.account_name)
            acct1.close_account()
            acct2.close_account()
            print("Account consolidated!")
            return new_account
        else:
            print("Accounts cannot be consolidated.")
            return None

# savings account and checking account are child classes of the parent class Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_balance, customer, bank):
        super().__init__(account_number, account_balance, customer, bank)

class CheckingAccount(Account):
    def __init__(self, account_number, account_balance, customer, bank):
        super().__init__(account_number, account_balance, customer, bank)

def display_menu(acc):
    print("Welcome, Account Number: ", acc.account_number)
    while True: 
        print("------------------MENU----------------")
        print("Option 1: View current balance\nOption 2: Withdraw money\nOption 3: Deposit money\nOption 4: Exit main menu")

        option = input("Enter your option now")

        if option == "1":
            print("You chose option 1: View current balance")
            acc.check_balance()

        elif option == "2":
            print("You chose option 2: Withdraw money")
            amount = float(input("Enter an amount to withdraw: "))
            acc.withdraw(amount)

        elif option == "3":
            print("You chose option 3: Deposit money")
            amount = float(input("Enter an amount to deposit: "))
            acc.deposit(amount)
        
        elif option == "4":
            print("You chose option 4: Exit main menu\nExiting the system")
            ID_prompt()
        else: 
            print("Enter a valid option")

def is_valid_ID(user_id):
    for acc in accounts_list:
        if acc.account_number == user_id:
            print(acc)
            return acc
    return False

def ID_prompt():
    while True:
        user_id = input("Please enter your ID")
        account = is_valid_ID(user_id)
        if account:
            # charge a $10 fee for using ATM
            account.charge_fee()
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

# Create 3 customers
cus1 = Customer("Alex", "P Sherman 42, Sydney")
print("Creating the following customer:\n", cus1)

cus2 = Customer("Bob", "Pineapple Drive, Atlantia")
print("Creating the following customer:\n", cus2)

cus3 = Customer("Harry", "Under, The Stair")
print("Creating the following customer:\n", cus3)

# Create 2 banks
bank1 = Bank("Lending Corp", "Wallstreet")
print("Creating the following bank:\n", bank1)

bank2 = Bank("Piggy Bank", "ChestofDrawer")
print("Creating the following bank:\n", bank2)

accounts_list = [Account(str(i), 100, cus1, bank1) for i in range(10)]

#Create 3 accounts to test functions
acct1 = Account(generate_random_account_number(), 100, cus2, bank2)
accounts_list.append(acct1)

acct2 = Account(generate_random_account_number(), 100, cus3, bank2)
accounts_list.append(acct2)

acct3 = Account(generate_random_account_number(), 100, cus1, bank2)
accounts_list.append(acct3)

# Test account count tracking. Should be 13
print(f"{Account.check_account_count} Active accounts")

# Test change name
acct1.change_name("Linda")
print(acct1)
acct2.change_name("Brad")
print(acct2)
acct3.change_name("Felix")
print(acct3)

# Test withdraw function
acct1.withdraw(70.3)
acct2.withdraw(55.34)
acct3.withdraw(30)

# Test deposit function
acct1.deposit(70.3)
acct2.deposit(55.34)
acct3.deposit(30)

# Test consolidation 
acct1.change_name("Brenda")
acct2.change_name("Brenda")
acct4 = Account.accountConsolidate(acct1, acct2)
print(acct4)

# Initiate ATM. Prompt user for ID. Display main menu
ID_prompt()

#Test withdraw method 