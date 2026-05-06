nums = [2, 5, 1, 8, 3]

max_diff = max(abs(nums[i] - nums[i - 1]) for i in range(1, len(nums)))
print(max_diff)