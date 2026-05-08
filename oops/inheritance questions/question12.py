### Assignment 12: Complex Multiple Inheritance

#Create a class named `Base1` with an attribute `a`. Create a class named `Base2` with an attribute `b`. Create a class named `Derived` that inherits from both `Base1` and `Base2` and adds an attribute `c`. Initialize all attributes using the `super()` function. Create an object of the `Derived` class and print its attributes.

class Base1:
    def __init__(self, a):
        self.a = a

class Base2:
    def __init__(self, b):
        self.b = b

class Derived(Base1, Base2):
    def __init__(self, a, b, c):
        super().__init__(a)
        Base2.__init__(self, b)
        self.c = c

# Test
derived = Derived(1, 2, 3)
print(derived.a, derived.b, derived.c)