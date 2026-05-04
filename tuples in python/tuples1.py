numbers=(1,2,3,4,5,6,6)
print(type(numbers))
print(numbers.count(6))
print(numbers.index(2))
numbers_tuple=(1,2,3,4)
mixed_tuple=("manasi",3.14,5)
concatenated_tuple=mixed_tuple+numbers_tuple
print(concatenated_tuple)
a,b,c=mixed_tuple
print(a)
print(b)
print(c)
first,*middle,last=numbers_tuple
print(first)
print(middle)
print(last)
list=[(1,2,3,4,5),('a','b','c'),(True,False)]
print(list[0])
print(list[1][2])
print(list[0][1:3])
for sublist in list:
    for item in sublist:
        print(item , end=" ")
    print()