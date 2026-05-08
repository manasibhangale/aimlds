### Assignment 11: Multiple Inheritance with Different Methods

#Create a class named `Flyer` with a method `fly` that prints a flying message. Create a class named `Swimmer` with a method `swim` that prints a swimming message. Create a derived class `Superhero` that inherits from both `Flyer` and `Swimmer`. Create an object of the `Superhero` class and call both methods.

class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Superhero(Flyer, Swimmer):
    pass

# Test
superhero = Superhero()
superhero.fly()
superhero.swim()