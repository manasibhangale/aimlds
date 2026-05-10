import multiprocessing   # Import multiprocessing module
import time              # Import time module

# Function to calculate squares
def square():
    for i in range(5):
        time.sleep(1)   # Pause execution for 1 second
        print(f"square: {i**2}")

# Function to calculate cubes
def cube():
    for i in range(5):
        time.sleep(1.5)   # Pause execution for 1.5 seconds
        print(f"cube: {i**3}")

# Main block
if __name__ == "__main__":

    # Start timer
    start_time = time.time()

    # Create processes
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to finish
    p1.join()
    p2.join()

    # Calculate total execution time
    finishing_time = time.time() - start_time

    # Print execution time
    print(f"\nExecution Time: {finishing_time:.2f} seconds")