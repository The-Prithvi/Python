class animal:
    no_of_animals = 0
    trainPow = 3
    def __init__(self, name, power, speed):
        self.name = name
        self.power = power
        self.speed = speed
        animal.no_of_animals += 1
    def increasePow(self):
        self.power = self.power + animal.trainPow

print(animal.no_of_animals)
horse = animal("Horse", 71, 89)
tiger = animal("Tiger", 78, 82)
dog = animal("Dog", 37, 55)
print(animal.no_of_animals)
print(dog.power)
dog.increasePow()
print(dog.power)
