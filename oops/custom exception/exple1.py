# Custom Exception Example

class InvalidAgeError(Exception):
    # Custom exception class
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    else:
        print("Eligible")


# Test
try:
    check_age(15)

except InvalidAgeError as e:
    print("Custom Exception Caught:", e)