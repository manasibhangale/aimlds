def rotate_right(lst, k):
    k = k % len(lst)   # handle k > length
    return lst[-k:] + lst[:-k]

# Example
nums = [1, 2, 3, 4, 5]
print(rotate_right(nums, 2))  # [4, 5, 1, 2, 3]