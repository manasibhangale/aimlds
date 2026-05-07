### Assignment 4: Class with Private Attributes
#Create a class named `BankAccount` with private attributes `account_number` and `balance`. Add methods to deposit and withdraw money, and to check the balance. Create an object of the class and perform some operations.

class BankAccount:
    def __init__(self,account_number,balance=0):
        self.__account_number=account_number
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance+=amount
        print(f"{amount} is deposited. new balance is {self.__balance}")

    def withdraw(self,amount):
        if amount>self.__balance:
            print(f"Insufficient balance")
        else:
            self.__balance-=amount
            print(f"{amount} is withdrawn. new balance is {self.__balance}")
    
    def check_balance(self):
        print(f"Balance is: {self.__balance}")


account = BankAccount('12345678', 1000)
account.deposit(500)
account.withdraw(200)
print(account.check_balance())  # 1300
account.withdraw(2000)  # Insufficient balance!