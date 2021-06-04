import random
import time
import datetime

def gen(limit):
    l = []

    for i in range(0, limit):
        nr = random.randint(-2147483648, 2147483648)
        l.append(nr)
    return l

def partition(l, low, high):

    i = low - 1
    pivot = l[high]

    for j in range(low, high):
        if l[j] <= pivot:
            i  += 1
            (l[i], l[j]) = (l[j], l[i])

    (l[i + 1], l[high]) = (l[high], l[i + 1])

    return i + 1

def quickSort(l, low, high):
    if len(l) == 1:
        return l

    if low < high:
        p = partition(l, low, high)

        quickSort(l, low, p - 1)
        quickSort(l, p + 1, high)

#liste mici
l1 = gen(100)

start = datetime.datetime.now()

quickSort(l1, 0, len(l1) - 1)

end = datetime.datetime.now()

time_diff = (end - start)
print("100 elemente:")
print(time_diff.total_seconds() * 1000) #milisecunde

l2 = gen(300)

start = datetime.datetime.now()

quickSort(l2, 0, len(l2) - 1)

end = datetime.datetime.now()

time_diff = (end - start)
print("300 elemente:")
print(time_diff.total_seconds() * 1000) #milisecunde

l3 = gen(500)

start = datetime.datetime.now()

quickSort(l3, 0, len(l3) - 1)

end = datetime.datetime.now()

time_diff = (end - start)
print("500 elemente:")
print(time_diff.total_seconds() * 1000) #milisecunde

#liste mari

#L1 = generate(1000)
L1 = gen(1000)

start = time.time()

quickSort(L1, 0, len(L1) - 1)

end = time.time()

print("1000 elemente:")
print(end - start) #secunde

#L2 = generate(10000)
L2 = gen(10000)

start = time.time()

quickSort(L2, 0, len(L2) - 1)

end = time.time()

print("10000 elemente:")
print(end - start) #secunde

#L3 = generate(100000)
L3 = gen(100000)

start = time.time()

quickSort(L3, 0, len(L3) - 1)

end = time.time()

print("100000 elemente:")
print(end - start) #secunde

#L4 = generate(1000000)
L4 = gen(1000000)

start = time.time()

quickSort(L4, 0, len(L4) - 1)

end = time.time()

print("1000000 elemente:")
print(end - start) #secunde

#L5 = generate(10000000)
L5 = gen(10000000)

start = time.time()

quickSort(L5, 0, len(L5) - 1)

end = time.time()

print("10000000 elemente:")
print(end - start) #secunde

