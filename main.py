
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

l = [8, 7, 12, 10, 2, 999, 45]
print(l)
mergeSort(l)
print(l)