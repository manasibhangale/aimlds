# Module: Iterators, Generators, and Decorators Assignments
## Lesson: Iterators, Generators, and Decorators
### Assignment 1: Custom Iterator

#Create a custom iterator class named `Countdown` that takes a number and counts down to zero. Implement the `__iter__` and `__next__` methods. Test the iterator by using it in a for loop.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current

# Test
for number in Countdown(5):
    print(number)