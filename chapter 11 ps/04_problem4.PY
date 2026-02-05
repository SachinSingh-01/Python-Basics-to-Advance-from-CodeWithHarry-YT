class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        real_part = self.r * other.r - self.i * other.i
        imag_part = self.r * other.i + self.i * other.r
        return Complex(real_part, imag_part)

    def __str__(self):
        sign = '+' if self.i >= 0 else '-'
        return f"{self.r} {sign} {abs(self.i)}i"

# Example usage:
c1 = Complex(1, 2)
c2 = Complex(3, 4)

print("c1 =", c1)
print("c2 =", c2)
print("c1 + c2 =", c1 + c2)
print("c1 * c2 =", c1 * c2)
