import random
import time
import datetime

def gen(limit):
    l = []

    for i in range(0, limit):
        nr = random.randint(-2147483648, 2147483648)
        l.append(nr)
    return l

def mergeSort(l):

    if len(l) > 1:
        mid = len(l) // 2

        L = l[:mid]
        R = l[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                l[k] = L[i]
                i += 1
            else:
                l[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            l[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            l[k] = R[j]
            j += 1
            k += 1

#liste mici
l1 = gen(100)

start = datetime.datetime.now()

mergeSort(l1)

end = datetime.datetime.now()

time_diff = (end - start)
print("100 elemente:")
print(time_diff.total_seconds() * 1000) #milisecunde

l2 = gen(300)

start = datetime.datetime.now()

mergeSort(l2)

end = datetime.datetime.now()

time_diff = (end - start)
print("300 elemente:")
print(time_diff.total_seconds() * 1000) #milisecunde

l3 = gen(500)

start = datetime.datetime.now()

mergeSort(l3)

end = datetime.datetime.now()

time_diff = (end - start)
print("500 elemente:")
print(time_diff.total_seconds() * 1000) #milisecunde

#liste mari

#L1 = generate(1000)
L1 = gen(1000)

start = time.time()

mergeSort(L1)

end = time.time()

print("1000 elemente:")
print(end - start) #secunde

#L2 = generate(10000)
L2 = gen(10000)

start = time.time()

mergeSort(L2)

end = time.time()

print("10000 elemente:")
print(end - start) #secunde

#L3 = generate(100000)
L3 = gen(100000)

start = time.time()

mergeSort(L3)

end = time.time()

print("100000 elemente:")
print(end - start) #secunde

#L4 = generate(1000000)
L4 = gen(1000000)

start = time.time()

mergeSort(L4)

end = time.time()

print("1000000 elemente:")
print(end - start) #secunde

#L5 = generate(10000000)
L5 = gen(10000000)

start = time.time()

mergeSort(L5)

end = time.time()

print("10000000 elemente:")
print(end - start) #secunde
