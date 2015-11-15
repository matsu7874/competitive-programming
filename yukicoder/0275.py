N = int(input())
A = list(map(int, input().split()))
A.sort()
print((A[N // 2] + A[(N - 1) // 2]) / 2)
