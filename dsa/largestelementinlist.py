nums = [10, 25, 5, 40, 15]

largest = nums[0]
for num in nums:
    if num > largest:
        largest = num

print(largest)  # 40
print(max(nums))