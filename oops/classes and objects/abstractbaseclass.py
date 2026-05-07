### Assignment 11: Abstract Base Class

#Create an abstract base class named `Shape` with an abstract method `area`. Create derived classes `Circle` and `Square` that implement the `area` method. Create objects of the derived classes and call the `area` method.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Test
circle = Circle(5)
square = Square(4)
print(circle.area())  # 78.53981633974483
print(square.area())  # 16