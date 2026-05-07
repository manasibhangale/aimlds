def valueerror():
    try:
        value=int(input("enter a number: "))
    except ValueError as ex:
        print(f"Error: {ex}")
        value=None
    finally:
        print("execution completed")
    return value
print(valueerror())