### Assignment 13: Class with Custom Exception

#Create a custom exception named `InsufficientBalanceError`. In the `BankAccount` class, raise this exception when a withdrawal amount is greater than the balance. Handle the exception and print an appropriate message.

class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient balance!")
        else:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance

# Test
account = BankAccount('12345678', 1000)
account.deposit(500)
try:
    account.withdraw(2000)
except InsufficientBalanceError as e:
     print(f"Error: {e}")