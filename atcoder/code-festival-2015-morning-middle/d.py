N, K = map(int, input().split())
A = list(map(int, input().split()))
B = [[A[i], i] for i in range(N)]
for i in range(K):
    B.sort()
    B[-1][0] -= 1
C = [[B[i][1], B[i][0]] for i in range(N)]
C.sort()
A = [0] + [C[i][1] for i in range(N)] + [0]
cnt = 0
for i in range(1, N + 1):
    cnt += A[i] * 2 + 1
    if A[i] > A[i - 1]:
        cnt += A[i] - A[i - 1]
    if A[i] > A[i + 1]:
        cnt += A[i] - A[i + 1]

print(cnt)
