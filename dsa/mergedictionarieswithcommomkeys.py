d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

result = {}

for key in set(d1) | set(d2):   # union of keys
    result[key] = d1.get(key, 0) + d2.get(key, 0)

print(result)
#2
from collections import Counter

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

result = dict(Counter(d1) + Counter(d2))
print(result)