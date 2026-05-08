### Assignment 8: Polymorphism with Inheritance

#Create a base class named `Animal` with a method `speak`. Create two derived classes `Dog` and `Cat` that override the `speak` method. Create a list of `Animal` objects and call the `speak` method on each object to demonstrate polymorphism.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("woof woof!")

class Cat(Animal):
    def speak(self):
        print("meow meow")

animals=[Cat(),Dog()]
for animal in animals:
    animal.speak()