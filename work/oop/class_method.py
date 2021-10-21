class animal:
    increase = 3
    def __init__(self, name, power, speed):
        self.name = name
        self.power = power
        self.speed = speed
    def increment(self):
        self.power = self.power + animal.increase

    @classmethod
    def change_increment(cls, inc):
        cls.increase = inc

horse = animal("Horse", 71, 89)
tiger = animal("Tiger", 78, 82)
dog = animal("Dog", 37, 55)
print(tiger.power)
animal.change_increment(5)
tiger.increment()
print(tiger.power)
