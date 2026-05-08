### Assignment 4: Multiple Inheritance Basic

#Create a base class named `Walker` with a method `walk` that prints a walking message. Create another base class named `Runner` with a method `run` that prints a running message. Create a derived class named `Athlete` that inherits from both `Walker` and `Runner`. Create an object of the `Athlete` class and call both methods.

class Walker:
    def walk(self):
        print("started walking")

class Runner:
    def run(self):
        print("started runing")

class Athelete(Walker,Runner):
    pass

athelete=Athelete()
athelete.walk()
athelete.run()