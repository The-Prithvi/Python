class animal:
    def __init__(self, name, power, speed):
        self.name = name
        self.power = power
        self.speed = speed
horse = animal("Horse", 71, 89)
tiger = animal("Tiger", 78, 82)
dog = animal("Dog", 37, 55)
print(dog.speed)
print(horse.power)
