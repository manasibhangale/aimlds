from concurrent.futures import ThreadPoolExecutor
import time

# Function to print numbers
def printnumbers(number):

    # Pause for 1 second
    time.sleep(1)

    # Print number
    print(number)

# List of numbers
number = [1,2,3,4,5,6,7,8,9]

# Create thread pool with 3 worker threads
with ThreadPoolExecutor(max_workers=3) as executor:

    # Execute function for each number
    results = executor.map(printnumbers, number)

# Print returned values
for result in results:
    print(result)