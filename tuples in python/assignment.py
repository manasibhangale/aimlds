tuple1=tuple(x for x in range(1,11))
print(tuple1)
print(tuple1[0])
print(tuple1[len(tuple1)//2])
print(tuple1[-1])
print(tuple1[0:3])
print(tuple1[1:5])
print(tuple1[-3:])
#nested tuple for 3x3 matrix
matrix=(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
print(f"the 2nd row 2nd column element is: {matrix[2][2]}")
tup1=(1,2,3)
tup2=(4,5,6)
print(tup1+tup2)