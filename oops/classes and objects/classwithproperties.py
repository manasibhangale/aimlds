### Assignment 10: Class with Properties

#Create a class named `Rectangle` with private attributes `length` and `width`. Use properties to get and set these attributes. Create an object of the class and test the properties.

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

# Test
rect = Rectangle(10, 5)
print(rect.length, rect.width)  # 10 5
rect.length = 15
rect.width = 7
print(rect.length, rect.width)  # 15 7