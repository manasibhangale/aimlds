class negativeNumberError(Exception):
    pass

def checkfornegatives(list):
    try:
        for item in list:
            if item<0:
                raise negativeNumberError(f"Negative number found: {item}")
            
    except negativeNumberError as e:
        print(f"Error: {e}")

    finally:
        print("execution completed")

list1=[1,2,3,4]
list2=[1,2,-3,4]
print(checkfornegatives(list1))
print(checkfornegatives(list2))