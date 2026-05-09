### Assignment 3: Generator Function

#Write a generator function named `fibonacci` that yields the Fibonacci sequence. Test the generator by iterating over it and printing the first 10 Fibonacci numbers.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Test
for num in fibonacci(10):
      print(num)