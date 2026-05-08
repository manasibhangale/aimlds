### Assignment 2: Polymorphism with Function Arguments

#Create a function named `describe_shape` that takes a `Shape` object as an argument and calls its `area` method. Create objects of `Circle` and `Square` classes and pass them to the `describe_shape` function.

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
    

def describe_shape(shape):
    print(f"The area of the shape is: {shape.area()}")

# Test
circle = Circle(5)
square = Square(4)
describe_shape(circle)
describe_shape(square)