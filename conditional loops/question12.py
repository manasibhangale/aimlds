num=int(input("enter a number:"))
originalnum=num
fact=1
while num!=0:
    fact=fact*num
    num=num-1
print(f"factorial of {originalnum} is {fact}")