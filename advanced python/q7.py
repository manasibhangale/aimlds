### Assignment 7: Decorator with Arguments

#Write a decorator named `repeat` that takes an argument `n` and repeats the execution of the decorated function `n` times. Apply this decorator to a function that prints a message.
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def print_message(message):
    print(message)

# Test
print_message("Hello, World!")