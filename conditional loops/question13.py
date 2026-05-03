num=int(input("enter a numer:"))
sum=0
originalnum=num
while num != 0:
    lastdigit=num%10
    sum=sum+lastdigit
    num=num//10
print(f"sum of all digits of {originalnum} is {sum}.")