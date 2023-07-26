import random

def randomizer(upper):
    num = random.randint(1,upper)
    return num

def randomDecimal():
    num = random.randint(1,100)
    num = num * .01
    return num