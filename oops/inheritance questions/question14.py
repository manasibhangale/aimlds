### Assignment 14: Polymorphism with Inheritance

#Create a base class named `Bird` with a method `speak`. Create two derived classes `Parrot` and `Penguin` that override the `speak` method. Create a list of `Bird` objects and call the `speak` method on each object to demonstrate polymorphism.

class Bird:
    def speak(self):
        pass

class Parrot(Bird):
    def speak(self):
        print("Parrot says: Squawk!")

class Penguin(Bird):
    def speak(self):
        print("Penguin says: Honk!")

# Test
birds = [Parrot(), Penguin()]
for bird in birds:
    bird.speak()