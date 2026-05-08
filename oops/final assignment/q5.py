### Assignment 5: Encapsulation with Private Attributes

#Create a class named `BankAccount` with private attributes `account_number` and `balance`. Add methods to deposit and withdraw money, and to check the balance. Ensure that the balance cannot be accessed directly.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance

# Test
account = BankAccount('12345678', 1000)
account.deposit(500)
account.withdraw(200)
print(account.check_balance())  # 1300
account.withdraw(2000)  # Insufficient balance