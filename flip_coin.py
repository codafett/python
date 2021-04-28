from random import random


def flip_coin():
    r = random()
    if r > 0.5:
        return "Heads"
    return "Tails"


print(flip_coin())