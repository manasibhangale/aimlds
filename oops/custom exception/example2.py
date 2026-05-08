class InvalidMarksError(Exception):
    pass


marks = int(input("Enter marks: "))

try:
    if marks > 100 or marks < 0:
        raise InvalidMarksError("Marks should be between 0 and 100")

    print("Valid Marks")

except InvalidMarksError as e:
    print(e)