import random
def addition(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

def gen_random(a, b):
    return random.randint(a, b)

def greet_gm(name):
    return "Hello and good morning Mr./Mrs./Ms.{}".format(name)