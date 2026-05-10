import math
import multiprocessing
import sys

# Function to calculate factorial
def factorial_number(n):
    return math.factorial(n)

if __name__ == "__main__":

    # Increase recursion/string limit if needed
    sys.set_int_max_str_digits(100000)

    # Numbers list
    numbers = [5, 10, 15, 20]

    # Create pool of worker processes
    with multiprocessing.Pool(processes=4) as pool:

        # Calculate factorials using pool
        results = pool.map(factorial_number, numbers)

    # Print results
    for number, result in zip(numbers, results):
        print(f"Factorial of {number} = {result}")