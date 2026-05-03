num=float(input("enter a number:"))
if num>0:
    if num%2==0:
        print(f"{num} is an even positive number.")
    else:
        print(f"{num} is an odd positive number.")
else:
    print(f"{num} is negative number.")