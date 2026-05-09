### Assignment 15: Generator Pipeline

#Write three generator functions: `integers` that yields integers from 1 to 10, `doubles` that yields each integer doubled, and `negatives` that yields the negative of each doubled value. Chain these generators to create a pipeline that produces the negative doubled values of integers from 1 to 10.

def integers():
    for i in range(1, 11):
        yield i

def doubles(numbers):
    for number in numbers:
        yield number * 2

def negatives(numbers):
    for number in numbers:
        yield -number

# Test
int_gen = integers()
double_gen = doubles(int_gen)
negative_gen = negatives(double_gen)
for value in negative_gen:
    print(value)