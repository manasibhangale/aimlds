def handlingdivisionbyzero(a, b):
    try:
        result = a / b

    except ZeroDivisionError as ex:
        print(f"Error: {ex}")
        result = None
        print("Denominator must be greater than zero")

    finally:
        print("Execution completed")

    return result


print(handlingdivisionbyzero(9, 3))
print(handlingdivisionbyzero(9, 0))