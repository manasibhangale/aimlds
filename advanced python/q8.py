### Assignment 8: Nested Decorators

#Write two decorators: `uppercase` that converts the result of a function to uppercase, and `exclaim` that adds an exclamation mark to the result of a function. Apply both decorators to a function that returns a greeting message.
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@uppercase
@exclaim
def greet(name):
    return f"Hello, {name}"

# Test
print(greet("Alice"))