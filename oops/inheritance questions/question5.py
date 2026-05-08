### Assignment 5: Method Resolution Order (MRO) in Multiple Inheritance

#In the `Athlete` class, override the `walk` method to print a different message. Create an object of the class and call the `walk` method. Use the `super()` function to call the `walk` method of the `Walker` class.

class Walker:
    def walk(self):
        print("started walking")

class Runner:
    def run(self):
        print("started runing")

class Athelete(Walker,Runner):
    def walk(self):
        print("athelete is walking")
        super().walk()

athelete=Athelete()
athelete.walk()
