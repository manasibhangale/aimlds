import threading
import time

def read_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"numbers: {i}")

def read_letters():
    for i in "abcd":
        time.sleep(2)
        print(f"letters: {i}")

# Create threads
t1 = threading.Thread(target=read_numbers)
t2 = threading.Thread(target=read_letters)

# Start timer
start_time = time.time()

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()

# End timer
end_time = time.time()

print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")