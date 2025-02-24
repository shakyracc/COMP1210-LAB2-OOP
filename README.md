## Section 1: Implementing Classes
Consider a class that represents a bank account.
1. Such a class might store information about the account balance, the name
of the account holder, and an account number. What instance variables
would you declare to hold this information? Give a type and name for
each.
2. There are a number of operations that would make sense for a bank account: withdraw money, deposit money, check the balance, and so on.
Write a function header with return type, name, and parameter list, for
each such operation described below. Don’t write the whole function, just
the header. They will all be public methods. The first one is done for you
as an example.
[X] - (a) Withdraw a given amount from the account. This changes the account balance, but does not return a value.

    `def withdraw ( self , amount ):`
[X]- (b) Deposit a given amount into the account. This changes the account
balance, but does not return a value.
[X]- (c) Get the balance from the account. This does not change anything in
the account; it simply returns the balance.
[X]- (d) Return a string containing the account information (name, account
number, balance). This does not change anything in the account.
[X] - (e) Charge a $10 fee. This changes the account balance but does not
return a value.
[X] - (f) Create a new account given an initial balance, the name of the owner,
and the account number. Note that this will be a constructor, and
that a constructor does not have a return type.
### Exercises
Use the Account class which simulates an ATM. Create 10 accounts in a list
with ID 0, 1, . . . , 9, and an initial balance of $100. The system prompts the
user to enter an ID. If the ID is entered incorrectly, ask the user to enter a
correct ID. Once an ID is accepted, the main menu is displayed as shown in
the sample run. You can enter choice 1 for viewing the current balance, 2 for
withdrawing money, 3 for depositing money, and 4 for exiting the main menu.
Once you exit, the system will prompt for an id again. Thus, once the system
starts, it will not stop.
[X] 1. Implement **chargeFee** function, which should deduct a service fee from
the account and return a new balance.
[X] 2. Implement **changeName** which takes a string as a parameter and changes
the name on the account to be that string.
[X] 3. Allow the account number to be randomly generated.
4. Suppose the bank wants to keep track of how many accounts exist. Implement this feature using a variable and function.
5. Add a **close** method to your **Account** class. This method should close
the current account by appending “CLOSED” to the account name and
setting the balance to 0.
6. Add a function **accountConsolidate(Account acct1, Account acct2)**
to your **Account** class that creates a new account whose balance is the sum
of the balances in **acct1** and **acct2** and closes **acct1** and **acct2**. The new
account should be returned. Two important rules of consolidation:
- (a) Only accounts with the same name can be consolidated. The new
account gets the name on the old accounts but a new account number.
- (b) Two accounts with the same number cannot be consolidated. Otherwise, this would be an easy way to double your money!
Check these conditions before creating the new account. If either condition
fails, do not create the new account or close the old ones; print a useful
message and return **None**.
Test your code to make sure it works. You should have at least 3 test cases for
each function.
## Section 2: Implementing Classes Relationships
1. A bank account has a balance, a customer, and an account number. A
customer has a name and an address. A bank has a name and an address.
Implement these classes and their relationships. (Hint: Use the **Account**
class from Section 1. Notice that some of the classes have a “has-a”
relationship, and some have an “is-a” relationship.)
2. There are different types of accounts: savings accounts, checking accounts,
and so on. What is the relationship between these classes and the **Account**
class? Modify your account class to include these classes and their relationships.