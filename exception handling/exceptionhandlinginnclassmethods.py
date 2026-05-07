class Calculator:
    def divide(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            result = None
        finally:
            print("Execution complete.")
        return result

# Test
calc = Calculator()
print(calc.divide(10, 2))  # 5.0
print(calc.divide(10, 0))  # None