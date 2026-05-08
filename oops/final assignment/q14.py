### Assignment 14: Polymorphism with Multiple Inheritance

#Create a class named `Flyer` with a method `fly`. Create a class named `Swimmer` with a method `swim`. Create a class named `Superhero` that inherits from both `Flyer` and `Swimmer` and overrides both methods. Create an object of the `Superhero` class and call both methods.
class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Superhero(Flyer, Swimmer):
    def fly(self):
        print("Superhero flying...")

    def swim(self):
        print("Superhero swimming...")

# Test
superhero = Superhero()
superhero.fly()
superhero.swim()