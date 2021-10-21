class comlex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __add__(self, other):
        return comlex(self.r + other.r, self.i + other.i)
    def __mul__(self, other):
        mul_r = (self.r * other.r) - (self.i * other.i)
        mul_i = (self.r * other.i) + (self.i * other.r)
        return comlex(mul_r, mul_i)
    def __str__(self):
        return "{} + {}i".format(self.r, self.i)
c1 = comlex(3, 2)
c2 = comlex(1, 7)
print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)
