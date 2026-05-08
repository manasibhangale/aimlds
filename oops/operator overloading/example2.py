class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Addition
    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imag + other.imag
        )

    # Subtraction
    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real,
            self.imag - other.imag
        )

    # Multiplication
    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)

        return ComplexNumber(real_part, imag_part)

    # Equality check
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    # String representation
    def __repr__(self):
        return f"{self.real} + {self.imag}i"


# Objects
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)

# Operations
print(c1 + c2)   # 6 + 8i
print(c1 - c2)   # -2 + -2i
print(c1 * c2)   # -7 + 22i
print(c1 == c2)  # False