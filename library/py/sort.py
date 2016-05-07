import random
import time


def bogosort(A):
    while any(A[i] > A[i + 1] for i in range(len(A) - 1)):
        random.shuffle(A)
    return A


def selectionsort(A):
    N = len(A)
    for i in range(N - 1):
        min_i = i
        for j in range(i + 1, N):
            if A[j] < A[min_i]:
                min_i = j
        if min_i > i:
            A[i], A[min_i] = A[min_i], A[i]
    return A


def bubblesort(A):
    N = len(A)
    for i in range(N - 1):
        for j in range(N-1,i,-1):
            if A[j - 1] > A[j]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A


def insertionsort(A):
    for i in range(1, len(A)):
        t = A[i]
        if A[i - 1] > t:
            j = i
            while (j > 0 and A[j - 1] > t):
                A[j] = A[j - 1]
                j -= 1
            A[j] = t
    return A


def quicksort(A):
    if len(A) < 1:
        return A
    pivot = A[0]
    left = []
    right = []
    for x in range(1, len(A)):
        if A[x] <= pivot:
            left.append(A[x])
        else:
            right.append(A[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right


def is_sorted(A):
    return all(A[i] <= A[i + 1] for i in range(len(A) - 1))

if __name__ == '__main__':
    N=int(input())
    print(N)
    A = [i for i in range(N)]
    random.shuffle(A)
    # print(A)

    if N<=10:
        start = time.time()
        B = bogosort(A[:])
        elapsed = time.time() - start
        print('bogo sort', elapsed, is_sorted(B))

    if N<=10000:
        start = time.time()
        B = bubblesort(A[:])
        elapsed = time.time() - start
        print('bubble sort', elapsed, is_sorted(B))

        start = time.time()
        B = selectionsort(A[:])
        elapsed = time.time() - start
        print('selection sort', elapsed, is_sorted(B))

        start = time.time()
        B = insertionsort(A[:])
        elapsed = time.time() - start
        print('insertion sort', elapsed, is_sorted(B))

    start = time.time()
    B = quicksort(A[:])
    elapsed = time.time() - start
    print('quick sort', elapsed, is_sorted(B))
