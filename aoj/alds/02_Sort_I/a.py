def bubbleSort(A):
    N = len(A)
    cnt = 0
    for i in range(N):
        for j in range(N - 1, i, -1):
            if A[j] < A[j - 1]:
                cnt += 1
                A[j], A[j - 1] = A[j - 1], A[j]
    print(*A)
    print(cnt)
N = int(input())
A = list(map(int, input().split()))
bubbleSort(A)
