'''
This is an Object Oriented programming example.
It demonstrates the concept of inheritance, encapsulation, data hiding and polymorphism
'''

#The parent class Bankaccount
class BankAccount:
    def _init_(self, account_holder, balance):
        self.account_holder = account_holder # Public attribute
        self.__balance = balance # Private attribute (Encapsulation)

#deposit () method
"""Allows deposit of money into the account."""
def deposit(self, amount):
    if amount > 0:
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")
    else:
        print("Deposit amount must be positive.")

#withdraw()method
"""Allows withdrawal of money from the account."""
def withdraw(self, amount):
    if 0 < amount <= self.__balance:
        self.__balance -= amount
        print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
    else:
        print("Insufficient funds or invalid amount.")

#get_balance()method
"""Allows viewing of balance (getter method)."""
def get_balance(self):
    return self.__balance
#end of parent class Bankaccount

# Inheritance: SavingsAccount extends BankAccount
class SavingsAccount(BankAccount):
    def _init_(self, account_holder, balance, interest_rate):
        '''Child construtor which uses the parent but also adds an attribute interest_rate'''
        super()._init_(account_holder, balance)  # Call parent constructor to define and set interest rate
        self.interest_rate = interest_rate #public attribute

    def apply_interest(self):
        """SavingAccount have a unique method that applies interest to the balance"""
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest of {interest} applied. New balance: {self.get_balance()}")

#child class Checking account
class CheckingAccount(BankAccount):
    def _init_(self, account_holder, balance, overdraft_limit):
        '''Child construtor which uses the parent but also adds an extra feature of  overdraft_limit'''
        super()._init_(account_holder, balance)
        #super refers to parent
        self.overdraft_limit = overdraft_limit  # Extra feature for CheckingAccount

    def withdraw(self, amount):
        """Overrides withdraw method to allow overdraft."""
        '''Polmorphism applies by having a child withdraw() method overide the parent withdraw() method to allow for the overdraft '''

        if amount <= (self.get_balance() + self.overdraft_limit):
            self.deposit(-amount)  #we will deposit a negative amount indicating an overdraft
            print(f"Overdraft allowed. Withdrawn: {amount}. Remaining balance: {self.get_balance()}")
        else:
            print("Withdrawal exceeds overdraft limit.")