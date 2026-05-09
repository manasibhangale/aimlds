### Assignment 13: Context Manager Decorator

#Write a decorator named `open_file` that manages the opening and closing of a file. Apply this decorator to a function that writes some text to a file.

def open_file(file_name, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_name, mode) as file:
                return func(file, *args, **kwargs)
        return wrapper
    return decorator

@open_file('sample.txt', 'w')
def write_to_file(file, text):
    file.write(text)

# Test
write_to_file('Hello, World!')