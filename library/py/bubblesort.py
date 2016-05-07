import random
import time


def bubblesort(A):
    N = len(A)
    for i in range(N - 1):
        for j in range(i , N):
            if A[j - 1] > A[j]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A

if __name__ == '__main__':
    A = [i for i in range(1000)]
    random.shuffle(A)
    # print(A)
    start = time.time()
    B = bubblesort(A[:])
    elapsed = time.time() - start
    print(B)
    print(elapsed)
