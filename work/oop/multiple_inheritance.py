class primary_student:
    school = "kv"
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def age_inc(self):
        self.roll += 1
class secondry_student:
    school = "sc"
    def __init__(self, branch, age):
        self.branch = branch
        self.age = age
    def age_inc(self):
        self.age += 1
class senior_student(primary_student, secondry_student):
    def __init__(self, yol):
        self.yol = yol

std1 = primary_student("yo", 99)
std2 = secondry_student("sci", 17)
std3 = senior_student(2019)
std3.name = "bunny"
std3.branch = "com"
std3.age = 18
std3.roll = 25

print(std3.school)
print(std3.name)
print(std3.branch)
print(std3.age)
std3.age_inc()
print(std3.age)
