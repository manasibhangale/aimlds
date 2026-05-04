lst=["manasi","gargee"]
print(type(lst))
xyz=["abc",3.14,0,True,'m']
print(xyz)
fruits=["apple","banana","cherry","litchi"]
fruits[1]="watermelon"
print(fruits)
fruits.append("banana")
print(fruits)
fruits.remove("watermelon")
print(fruits)
fruits.pop()
print(fruits)
print(fruits[1:])
fruits.insert(1,"coconut")
print(fruits)
index=fruits .index("cherry")
print(index)
fruits.insert(3,"cherry")
print(fruits)
print(fruits.count("cherry"))
fruits.sort() #ascending
print(fruits)
fruits.reverse() #reverse the list
print(fruits)
fruits.clear()
print(fruits)