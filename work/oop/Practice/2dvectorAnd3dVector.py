class c2dvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def info(self):
        print("{}i, {}j".format(self.i, self.j))
class c3dvector(c2dvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def info(self):
        print("{}i, {}j, {}k".format(self.i, self.j, self.k))

v1 = c2dvector(2, 5)
v2 = c3dvector(1, 3, 9)
v1.info()
v2.info()
