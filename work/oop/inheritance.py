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

class reptile(animal):
    def __init__(self, name, power, speed, legs, can_swim):
        super().__init__(name, power, speed)
        self.legs = legs
        self.can_swim = can_swim
    def increasePow(self):
        self.power = self.power + animal.trainPow + 2



print(animal.no_of_animals)
horse = animal("Horse", 71, 80)
tiger = animal("Tiger", 78, 89)
dog = animal("Dog", 37, 62)
crocodile = reptile("Crocodile", 75, 36, 4, "Yes")
snake = reptile("Python", 31, 68, 0, "Yes")
print(animal.no_of_animals)
print(dog.power)
dog.increasePow()
print(dog.power)
print(snake.name, snake.can_swim, snake.power, snake.legs)
snake.increasePow()
print(snake.power)
