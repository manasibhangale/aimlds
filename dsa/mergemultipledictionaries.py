#1
d1 = {"a": 1}
d2 = {"b": 2}
d3 = {"c": 3}

result = {}
result.update(d1)
result.update(d2)
result.update(d3)

print(result)
#2
d1 = {"a": 1}
d2 = {"b": 2}
d3 = {"c": 3}

result = {**d1, **d2, **d3}
print(result)
#3
d1 = {"a": 1}
d2 = {"b": 2}
d3 = {"c": 3}

result = d1 | d2 | d3
print(result)