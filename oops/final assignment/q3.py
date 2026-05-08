### Assignment 3: Abstract Base Class with Abstract Methods

#Create an abstract base class named `Vehicle` with an abstract method `start_engine`. Create derived classes `Car` and `Bike` that implement the `start_engine` method. Create objects of the derived classes and call the `start_engine` method.

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("car engine starts..")

class Bike(Vehicle):
    def start_engine(self):
        print("bike engine starts..")

car = Car()
bike = Bike()
car.start_engine()
bike.start_engine()