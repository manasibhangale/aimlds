def convert_to_integers(lst):
    integers = []
    try:
        for item in lst:
            integers.append(int(item))
    except ValueError as e:
        print(f"Error: {e}")
        integers = None
    finally:
        print("Execution complete.")
    return integers

# Test
print(convert_to_integers(['1', '2', 'three', '4']))  # None
print(convert_to_integers(['1', '2', '3', '4']))  # [1, 2, 3, 4]