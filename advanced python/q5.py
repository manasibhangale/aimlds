### Assignment 5: Chaining Generators

#Write two generator functions: `even_numbers` that yields even numbers up to a limit, and `squares` that yields the square of each number from another generator. Chain these generators to produce the squares of even numbers up to 20.
def even_numbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i

def squares(numbers):
    for number in numbers:
        yield number * number

# Test
even_gen = even_numbers(20)
square_gen = squares(even_gen)
for square in square_gen:
     print(square)