# ====================================================================================
# COMPLETE NUMPY CHEAT SHEET WITH COMMENTS & OUTPUTS
# ====================================================================================

import numpy as np


# ====================================================================================
# 1. ARRAY CREATION METHODS
# ====================================================================================

# Create array
a = np.array([1,2,3])
print(a)

# Output:
# [1 2 3]


# Zeros array
print(np.zeros((2,3)))

# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]


# Ones array
print(np.ones((2,2)))

# Output:
# [[1. 1.]
#  [1. 1.]]


# Empty array
print(np.empty((2,2)))

# Output:
# Random garbage values


# Full array
print(np.full((2,2), 7))

# Output:
# [[7 7]
#  [7 7]]


# Identity matrix
print(np.eye(3))

# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


# Identity matrix using identity()
print(np.identity(3))

# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


# Diagonal matrix
print(np.diag([1,2,3]))

# Output:
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]


# arange(start, stop, step)
print(np.arange(1,10,2))

# Output:
# [1 3 5 7 9]


# linspace(start, stop, no_of_values)
print(np.linspace(0,10,5))

# Output:
# [ 0.   2.5  5.   7.5 10. ]


# logspace
print(np.logspace(1,3,5))

# Output:
# [  10.           31.6227766   100.          316.22776602 1000.        ]


# geomspace
print(np.geomspace(1,1000,4))

# Output:
# [   1.   10.  100. 1000.]


# Random values between 0 and 1
print(np.random.rand(2,2))

# Output:
# Random values


# Random normal distribution values
print(np.random.randn(2,2))

# Output:
# Random values


# Random integers
print(np.random.randint(1,10,5))

# Output:
# Example:
# [2 5 1 9 4]


# Random choice
print(np.random.choice([1,2,3,4],2))

# Output:
# Example:
# [2 4]


# ====================================================================================
# 2. ARRAY ATTRIBUTES
# ====================================================================================

arr = np.array([[1,2,3],[4,5,6]])

# Shape
print(arr.shape)

# Output:
# (2, 3)


# Number of dimensions
print(arr.ndim)

# Output:
# 2


# Total elements
print(arr.size)

# Output:
# 6


# Datatype
print(arr.dtype)

# Output:
# int64


# Size of one element
print(arr.itemsize)

# Output:
# 8


# Total bytes
print(arr.nbytes)

# Output:
# 48


# Transpose
print(arr.T)

# Output:
# [[1 4]
#  [2 5]
#  [3 6]]


# ====================================================================================
# 3. DATA TYPES & TYPE CONVERSION
# ====================================================================================

print(arr.astype(float))

# Output:
# [[1. 2. 3.]
#  [4. 5. 6.]]


print(arr.astype(str))

# Output:
# [['1' '2' '3']
#  ['4' '5' '6']]


# ====================================================================================
# 4. RESHAPING METHODS
# ====================================================================================

arr = np.arange(1,7)

print(arr.reshape(2,3))

# Output:
# [[1 2 3]
#  [4 5 6]]


print(arr.flatten())

# Output:
# [1 2 3 4 5 6]


print(arr.ravel())

# Output:
# [1 2 3 4 5 6]


print(np.expand_dims(arr, axis=0))

# Output:
# [[1 2 3 4 5 6]]


print(np.squeeze([[1,2,3]]))

# Output:
# [1 2 3]


# ====================================================================================
# 5. INDEXING & SLICING
# ====================================================================================

arr = np.array([10,20,30,40,50])

print(arr[0])

# Output:
# 10


print(arr[-1])

# Output:
# 50


print(arr[1:4])

# Output:
# [20 30 40]


print(arr[::-1])

# Output:
# [50 40 30 20 10]


# ====================================================================================
# 6. ITERATION METHODS
# ====================================================================================

arr = np.array([[1,2],[3,4]])

for i in arr:
    print(i)

# Output:
# [1 2]
# [3 4]


for j in np.nditer(arr):
    print(j)

# Output:
# 1
# 2
# 3
# 4


# ====================================================================================
# 7. MATHEMATICAL OPERATIONS
# ====================================================================================

a = np.array([1,2,3])
b = np.array([4,5,6])


# Addition
print(np.add(a,b))

# Output:
# [5 7 9]


# Subtraction
print(np.subtract(a,b))

# Output:
# [-3 -3 -3]


# Multiplication
print(np.multiply(a,b))

# Output:
# [ 4 10 18]


# Division
print(np.divide(a,b))

# Output:
# [0.25 0.4  0.5 ]


# Square
print(np.square(a))

# Output:
# [1 4 9]


# Square root
print(np.sqrt(a))

# Output:
# [1.         1.41421356 1.73205081]


# Absolute value
print(np.abs([-1,-2,-3]))

# Output:
# [1 2 3]


# ====================================================================================
# 8. ROUNDING METHODS
# ====================================================================================

arr = np.array([1.2, 2.7, 3.5])

print(np.round(arr))

# Output:
# [1. 3. 4.]


print(np.floor(arr))

# Output:
# [1. 2. 3.]


print(np.ceil(arr))

# Output:
# [2. 3. 4.]


# ====================================================================================
# 9. LOGARITHMIC & EXPONENTIAL
# ====================================================================================

arr = np.array([1,2,3])

print(np.exp(arr))

# Output:
# Exponential values


print(np.log(arr))

# Output:
# [0.         0.69314718 1.09861229]


print(np.log10(arr))

# Output:
# [0.         0.30103    0.47712125]


# ====================================================================================
# 10. TRIGONOMETRIC FUNCTIONS
# ====================================================================================

angles = np.array([0, np.pi/2, np.pi])

print(np.sin(angles))

# Output:
# [0.0000000e+00 1.0000000e+00 1.2246468e-16]


print(np.cos(angles))

# Output:
# [ 1.000000e+00  6.123234e-17 -1.000000e+00]


# ====================================================================================
# 11. STATISTICAL METHODS
# ====================================================================================

data = np.array([1,2,3,4,5])

print(np.mean(data))

# Output:
# 3.0


print(np.median(data))

# Output:
# 3.0


print(np.std(data))

# Output:
# 1.4142135623730951


print(np.var(data))

# Output:
# 2.0


print(np.min(data))

# Output:
# 1


print(np.max(data))

# Output:
# 5


print(np.sum(data))

# Output:
# 15


# ====================================================================================
# 12. NORMALIZATION
# ====================================================================================

mean = np.mean(data)
std = np.std(data)

normalized = (data - mean) / std

print(normalized)

# Output:
# [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]

# Formula:

::contentReference[oaicite:0]{index=0}



# ====================================================================================
# 13. SORTING & SEARCHING
# ====================================================================================

arr = np.array([5,2,8,1])

print(np.sort(arr))

# Output:
# [1 2 5 8]


print(np.argmax(arr))

# Output:
# 2


print(np.argmin(arr))

# Output:
# 3


print(np.where(arr > 3))

# Output:
# (array([0,2]),)


# ====================================================================================
# 14. BOOLEAN FILTERING
# ====================================================================================

arr = np.array([1,2,3,4,5])

print(arr[arr > 2])

# Output:
# [3 4 5]


# ====================================================================================
# 15. JOINING ARRAYS
# ====================================================================================

a = np.array([1,2])
b = np.array([3,4])

print(np.concatenate((a,b)))

# Output:
# [1 2 3 4]


print(np.vstack((a,b)))

# Output:
# [[1 2]
#  [3 4]]


# ====================================================================================
# 16. UNIQUE VALUES
# ====================================================================================

arr = np.array([1,2,2,3,3,4])

print(np.unique(arr))

# Output:
# [1 2 3 4]


# ====================================================================================
# 17. MATRIX OPERATIONS
# ====================================================================================

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.dot(a,b))

# Output:
# [[19 22]
#  [43 50]]


print(np.linalg.det(a))

# Output:
# -2.0


print(np.linalg.inv(a))

# Output:
# [[-2.   1. ]
#  [ 1.5 -0.5]]


# ====================================================================================
# 18. RANDOM METHODS
# ====================================================================================

np.random.seed(1)

print(np.random.randint(1,10,5))

# Output:
# Example:
# [6 9 6 1 1]


# ====================================================================================
# 19. STRING METHODS
# ====================================================================================

str_arr = np.array(['apple','banana'])

print(np.char.upper(str_arr))

# Output:
# ['APPLE' 'BANANA']


print(np.char.capitalize(str_arr))

# Output:
# ['Apple' 'Banana']


# ====================================================================================
# 20. NaN METHODS
# ====================================================================================

arr = np.array([1,np.nan,3])

print(np.isnan(arr))

# Output:
# [False  True False]


print(np.nanmean(arr))

# Output:
# 2.0


# ====================================================================================
# 21. SET OPERATIONS
# ====================================================================================

a = np.array([1,2,3])
b = np.array([3,4,5])

print(np.union1d(a,b))

# Output:
# [1 2 3 4 5]


print(np.intersect1d(a,b))

# Output:
# [3]


# ====================================================================================
# END OF NUMPY CHEAT SHEET
# ====================================================================================