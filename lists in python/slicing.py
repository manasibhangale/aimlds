lst=[1,2,3,4,5,6,7,8,9]
print(lst[1:])
print(lst[:5])
print(lst[1:3])
print(lst[:])
print(lst[::-1])
print(lst[::2])
print(lst[::-2])
print(lst[4:])
for num in lst:
    print(num, end=" ")
print()
for index,num in enumerate(lst):
    print(index,num)
lst1=[]
for i in range(10):
    lst1.append(i**2)
print(lst1)
print([x**2 for x in range(10)])
print([i for i in range(10) if i%2==0])
list1=[1,2,3,4]
list2=['a','b','c','d']
print([[i,j] for i in  list1 for j in  list2])
list3=("manasi","gargee","mukesh")
print([len(word) for word in list3])