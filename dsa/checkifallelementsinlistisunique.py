nums = [1, 2, 3, 4, 5]

is_unique = len(nums) == len(set(nums))
print(is_unique)  # True
#2
nums = [1, 2, 3, 2]

seen = set()
is_unique = True

for num in nums:
    if num in seen:
        is_unique = False
        break
    seen.add(num)

print(is_unique)  # False