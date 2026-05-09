### Assignment 12: Generator with Exception Handling

#Write a generator function named `safe_divide` that takes a list of numbers and yields the division of each number by a given divisor. Implement exception handling within the generator to handle division by zero.

def safe_divide(numbers, divisor):
    for number in numbers:
        try:
            yield number / divisor
        except ZeroDivisionError:
            yield "Error: Division by zero"

# Test
numbers = [10, 20, 30, 40]
for result in safe_divide(numbers, 0):
     print(result)