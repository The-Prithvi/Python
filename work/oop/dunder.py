class animal:
    def __init__(self, name, power, speed):
        self.name = name
        self.power = power
        self.speed = speed
    def __add__(self, other):
        return self.speed + other.speed
    def __repr__(self):
        return "Animal ({}, {}, {})".format(self.name, self.power, self.speed)
    def __str__(self):
        return "The name of the animal is {}".format(self.name)

horse = animal("Horse", 71, 89)
tiger = animal("Tiger", 78, 82)
dog = animal("Dog", 37, 55)
print(horse + tiger)
print(repr(tiger))
print(str(horse))


