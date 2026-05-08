### Assignment 13: Checking Instance Types with Inheritance

#Create a base class named `Animal` and a derived class named `Cat`. Create objects of both classes and use the `isinstance` function to check the instance types.

class Animal:
    pass

class Cat(Animal):
    pass

# Test
animal = Animal()
cat = Cat()
print(isinstance(animal, Animal))  # True
print(isinstance(cat, Animal))  # True
print(isinstance(cat, Cat))  # True
print(isinstance(animal, Cat))  # False