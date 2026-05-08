### Assignment 4: Abstract Base Class with Concrete Methods

#In the `Vehicle` class, add a concrete method `fuel_type` that returns a generic fuel type. Override this method in `Car` and `Bike` classes to return specific fuel types. Create objects of the derived classes and call the `fuel_type` method.

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def fuel_type(self):
        print("generic fuel")

class Car(Vehicle):
    def start_engine(self):
        print("car engine starts..")
    def fuel_type(self):
        print("CNG")

class Bike(Vehicle):
    def start_engine(self):
        print("bike engine starts..")
    def fule_type(self):
        print("petrol")

car = Car()
bike = Bike()
car.start_engine()
bike.start_engine()
car.fuel_type()
bike.fuel_type()