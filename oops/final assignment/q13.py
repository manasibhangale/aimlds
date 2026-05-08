### Assignment 13: Encapsulation in Class Hierarchies

#Create a base class named `Account` with private attributes `account_number` and `balance`. Add methods to get and set these attributes. Create a derived class named `SavingsAccount` that adds an attribute `interest_rate`. Create an object of the `SavingsAccount` class and test the encapsulation.

class Account:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

# Test
savings = SavingsAccount('12345678', 1000, 0.05)
print(savings.get_account_number(), savings.get_balance(), savings.interest_rate)
savings.set_balance(1500)
print(savings.get_account_number(), savings.get_balance(), savings.interest_rate)