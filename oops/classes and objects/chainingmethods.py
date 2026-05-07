### Assignment 15: Chaining Methods

#Create a class named `Calculator` with methods to add, subtract, multiply, and divide. Each method should return the object itself to allow method chaining. Create an object and chain multiple method calls.

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, amount):
        self.value += amount
        return self

    def subtract(self, amount):
        self.value -= amount
        return self

    def multiply(self, amount):
        self.value *= amount
        return self

    def divide(self, amount):
        if amount != 0:
            self.value /= amount
        else:
            print("Cannot divide by zero!")
        return self

# Test
calc = Calculator()
calc.add(10).subtract(3).multiply(2).divide(2)
print(calc.value)  # 7.0