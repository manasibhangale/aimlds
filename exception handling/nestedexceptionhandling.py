def nested_exception_handling(s):
    try:
        try:
            num = int(s)
        except ValueError as e:
            print(f"Conversion error: {e}")
            num = None
        finally:
            print("Conversion attempt complete.")
        if num is not None:
            try:
                result = 10 / num
            except ZeroDivisionError as e:
                print(f"Division error: {e}")
                result = None
            finally:
                print("Division attempt complete.")
            return result
    finally:
        print("Overall execution complete.")

# Test
print(nested_exception_handling('0'))  # None
print(nested_exception_handling('a'))  # None
print(nested_exception_handling('2'))  # 5.0