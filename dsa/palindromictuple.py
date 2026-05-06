#1
def is_palindrome_tuple(t):
    n = len(t)
    for i in range(n // 2):
        if t[i] != t[n - i - 1]:
            return False
    return True
#2
def is_palindrome_tuple(t):
    return t == t[::-1]

print(is_palindrome_tuple((1, 2, 3, 2, 1)))  # True
print(is_palindrome_tuple((1, 2, 3)))        # False