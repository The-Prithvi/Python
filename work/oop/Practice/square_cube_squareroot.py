class calculator:
    def __init__(self, num):
        self.num = num
    def square(self):
        print(self.num * self.num)
    def cube(self):
        print(self.num * self.num * self.num)
    def squareroot(self):
        print(self.num ** 0.5)

n = calculator(5)
n.cube()
n.square()
n.squareroot()