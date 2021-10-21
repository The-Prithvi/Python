class animal:
    def __init__(self, name, power, speed):
        self.name = name
        self.power = power
        self.speed = speed

    @classmethod
    def from_str(cls, animal_str):
        name, power, speed = animal_str.split(", ")
        return cls(name, power, speed)

horse = animal("Horse", 71, 89)
tiger = animal("Tiger", 78, 82)
dog = animal("Dog", 37, 55)
giraffe = animal.from_str("Giraffe, 68, 58")
print(giraffe.speed, giraffe.power, giraffe.name)

