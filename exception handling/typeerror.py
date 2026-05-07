def typeerror(lst):
    total=0
    try:
        for num in lst:
            total += num

    except TypeError as ex:
        print(f"Error : {ex}")
        total=None

    finally:
        print("execution completed")
    return total
list1=[1,2,3,4]
list2=[1,2,'a']
print(typeerror(list1))
print(typeerror(list2))