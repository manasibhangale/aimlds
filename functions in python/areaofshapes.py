import math

def area_circle(r):
    return math.pi * r * r

def area_rectangle(l, w):
    return l * w

def area_triangle(b, h):
    return 0.5 * b * h

def area_square(s):
    return s * s

def area_parallelogram(b, h):
    return b * h

def area_trapezium(a, b, h):
    return 0.5 * (a + b) * h


# Example usage
print("Circle:", area_circle(5))
print("Rectangle:", area_rectangle(4, 6))
print("Triangle:", area_triangle(3, 8))
print("Square:", area_square(4))
print("Parallelogram:", area_parallelogram(5, 7))
print("Trapezium:", area_trapezium(3, 5, 4))