import random


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

if __name__ == '__main__':
    A = [i for i in range(100)]
    random.shuffle(A)
    print(A)
    B = selectionsort(A[:])
    print(B)
