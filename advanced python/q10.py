### Assignment 10: Iterator Protocol with Decorators

#Create a custom iterator class named `ReverseString` that iterates over a string in reverse. Write a decorator named `uppercase` that converts the string to uppercase before reversing it. Apply the decorator to the `ReverseString` class.

def uppercase(cls):
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.data = self.data.upper()
    return Wrapped

@uppercase
class ReverseString:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Test
for char in ReverseString("hello"):
     print(char)