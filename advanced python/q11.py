### Assignment 11: Stateful Generators

#Write a stateful generator function named `counter` that takes a start value and increments it by 1 each time it is called. Test the generator by iterating over it and printing the first 10 values.
def counter(start):
    current = start
    while True:
        yield current
        current += 1

# Test
count = counter(0)
for _ in range(10):
     print(next(count))