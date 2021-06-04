import random

def gen(limit):
    l = []

    for i in range(0, limit):
        nr = random.randint(-2147483648, 2147483648)
        l.append(nr)
    return l

a = gen(100)
print(a)
