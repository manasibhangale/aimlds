def risky_function():
    raise ValueError("An error occurred in risky_function.")

def safe_function():
    try:
        risky_function()
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Execution complete.")

# Test
safe_function()  # Error: An error occurred in risky_function.