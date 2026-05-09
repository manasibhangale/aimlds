### Assignment 6: Simple Decorator

#Write a decorator named `time_it` that measures the execution time of a function. Apply this decorator to a function that calculates the factorial of a number.
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@time_it
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test
print(factorial(10))