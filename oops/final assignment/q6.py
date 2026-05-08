### Assignment 6: Encapsulation with Property Decorators

#In the `BankAccount` class, use property decorators to get and set the `balance` attribute. Ensure that the balance cannot be set to a negative value.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount

# Test
account = BankAccount('12345678', 1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)  # 1300
account.balance = -500  # Balance cannot be negative!