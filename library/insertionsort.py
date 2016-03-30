import random


def insertionsort(A):
    for i in range(1, len(A)):
        t = A[i]
        if A[i - 1] > t:
            j = i
            while (j > 0 and A[j - 1] > t):
                A[j] = A[j-1]
                j -= 1
            A[j] = t
    return A

if __name__ == '__main__':
    A = [i for i in range(30)]
    random.shuffle(A)
    print(A)
    B = insertionsort(A[:])
    print(B)
