### Assignment 8: Class with Class Variables

#Create a class named `Counter` with a class variable `count`. Each time an object is created, increment the count. Add a method to get the current count. Create multiple objects and print the count.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.get_count())  # 3