class vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        str = ""
        index = 0
        for i in self.vec:
            str += "{}a{} + ".format(i, index)
            index += 1
        return str[:-2]

    def __add__(self, other):
        li = []
        for i in range(0, len(self.vec)):
            li.append(self.vec[i] + other.vec[i])
        return vector(li)

    def __mul__(self, other):
        li = []
        a = 0
        b = 0
        while b != len(self.vec):
            for i in range(0, len(other.vec)):
                a += self.vec[b] * other.vec[i]
            li.append(a)
            a = 0
            b += 1
        return vector(li)

v1 = vector([2, 6, 7])
v2 = vector([7, 5, 4])
print(v1)
print(v2)
print(v1 + v2)
print(v1 * v2)