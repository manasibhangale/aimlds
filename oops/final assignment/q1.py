# Module: OOP Assignments
## Lesson: Polymorphism, Abstraction, and Encapsulation
### Assignment 1: Polymorphism with Methods

#Create a base class named `Shape` with a method `area`. Create two derived classes `Circle` and `Square` that override the `area` method. Create a list of `Shape` objects and call the `area` method on each object to demonstrate polymorphism.
import math
class Shape:
    def area():
        pass
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    
class Square:
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
    
shapes=[Circle(5),Square(5)]
for shape in shapes:
    print(shape.area())
    