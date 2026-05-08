### Assignment 10: Method Overriding and `super()`

#Create a class named `Vehicle` with a method `start` that prints a starting message. Create a derived class `Car` that overrides the `start` method to print a different message. Use the `super()` function to call the `start` method of the `Vehicle` class. Create an object of the `Car` class and call the `start` method.

class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Car(Vehicle):
    def start(self):
        print("Car starting...")
        super().start()

# Test
car = Car()
car.start()