from concurrent.futures import ProcessPoolExecutor
import time
def squares(numbers):
    time.sleep(1)
    print (f"square{numbers**2}")
numbers=[1,2,3,4,5]
if __name__=="__main__":
    with ProcessPoolExecutor (max_workers=3) as executor:
        results=executor.map(squares,numbers)
    for result in results:
        print(result)