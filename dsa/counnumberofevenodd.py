nums = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
#2
nums = [1, 2, 3, 4, 5, 6]

even = sum(1 for x in nums if x % 2 == 0)
odd = sum(1 for x in nums if x % 2 != 0)

print("Even:", even)
print("Odd:", odd)