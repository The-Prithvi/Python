class ronaldo:
    speacial = "Long Ranger"
    def __init__(self, shoot, pace):
        self.shoot = shoot
        self.pace = pace
    def det(self):
        return "Shoot: {}, Pace: {}, Specialaty: {}".format(self.shoot, self.pace, self.speacial)

class ronadojr(ronaldo):
        speacial = "Flair"
        def __init__(self, shoot, pace):
            super().__init__(shoot, pace)

class ronado2jr(ronadojr):
        # speacial = "Vision"
        def __init__(self, shoot, pace):
            super().__init__(shoot, pace)

p1 = ronaldo(93, 89)
print(p1.det())
p2 = ronadojr(82, 81)
print(p2.det())
p3 = ronado2jr(78, 76)
print(p3.det())

p2.speacial = "Attacking runner"
print(p2.det())

print(p3.det())
