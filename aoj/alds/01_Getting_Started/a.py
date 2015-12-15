def insertionsSort(A):
    print(*A)
    N = len(A)
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        print(*A)

N = int(input())
A = list(map(int, input().split()))
insertionsSort(A)
