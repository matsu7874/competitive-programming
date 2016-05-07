import random


def bogosort(A):
    while any(A[i]>A[i+1] for i in range(len(A)-1)):
        random.shuffle(A)
    return A

if __name__ == '__main__':
    A = [i for i in range(6)]
    random.shuffle(A)
    print(A)
    B = bogosort(A[:])
    print(B)
