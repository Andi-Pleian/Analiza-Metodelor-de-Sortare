import random
import time
import datetime

def gen(limit):
    l = []

    for i in range(0, limit):
        nr = random.randint(-2147483648, 2147483648)
        l.append(nr)
    return l

def bubbleSort(l):
    for i in range(len(l), 0, -1):
        for j in range(0, i - 1):
            if l[j] > l[j + 1]:
                aux = l[j]
                l[j] = l[j + 1]
                l[j + 1] = aux

#liste mici
l1 = gen(100)

start = datetime.datetime.now()

bubbleSort(l1)

end = datetime.datetime.now()

time_diff = (end - start)
print("100 elemente:")
print(time_diff.total_seconds() * 1000) #milisecunde

l2 = gen(300)

start = datetime.datetime.now()

bubbleSort(l2)

end = datetime.datetime.now()

time_diff = (end - start)
print("300 elemente:")
print(time_diff.total_seconds() * 1000) #milisecunde

l3 = gen(500)

start = datetime.datetime.now()

bubbleSort(l3)

end = datetime.datetime.now()

time_diff = (end - start)
print("500 elemente:")
print(time_diff.total_seconds() * 1000) #milisecunde

#liste mari

#L1 = generate(1000)
L1 = gen(1000)

start = time.time()

bubbleSort(L1)

end = time.time()

print("1000 elemente:")
print(end - start) #secunde

#L2 = generate(10000)
L2 = gen(10000)

start = time.time()

bubbleSort(L2)

end = time.time()

print("10000 elemente:")
print(end - start) #secunde

#L3 = generate(100000)
L3 = gen(100000)

start = time.time()

bubbleSort(L3)

end = time.time()

print("100000 elemente:")
print(end - start) #secunde

#L4 = generate(1000000)
L4 = gen(1000000)

start = time.time()

bubbleSort(L4)

end = time.time()

print("1000000 elemente:")
print(end - start) #secunde

#L5 = generate(10000000)
L5 = gen(10000000)

start = time.time()

bubbleSort(L5)

end = time.time()

print("10000000 elemente:")
print(end - start) #secunde

