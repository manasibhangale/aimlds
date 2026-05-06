#1
def merge_sorted_lists(a, b):
    i, j = 0, 0
    merged = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # Add remaining elements
    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged


# Example
a = [1, 3, 5]
b = [2, 4, 6]

print(merge_sorted_lists(a, b))
#2
a = [1, 3, 5]
b = [2, 4, 6]

merged = sorted(a + b)
print(merged)
#3
import heapq

a = [1, 3, 5]
b = [2, 4, 6]

merged = list(heapq.merge(a, b))
print(merged)