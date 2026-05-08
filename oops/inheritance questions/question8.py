### Assignment 8: Using `super()` in Single Inheritance

#Create a base class named `Shape` with an attribute `color`. Create a derived class named `Circle` that inherits from `Shape` and adds an attribute `radius`. Use the `super()` function to initialize the attributes. Create an object of the `Circle` class and print its attributes.

class Shape:
    def __init__(self,color):
        self.color=color

class Circle(Shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius=radius

circle = Circle("blue", 5)
print(circle.color, circle.radius)