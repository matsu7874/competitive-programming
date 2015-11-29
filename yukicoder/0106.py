N, K = map(int, input().split())
A = [0 for i in range(N + 1)]
for i in range(2, N + 1, 2):
    A[i] += 1
for i in range(3, N + 1, 2):
    if A[i] > 0:
        continue
    j = 1
    while i * j <= N:
        A[i * j] += 1
        j += 1
cnt = 0
for i in range(2, N + 1):
    if A[i] >= K:
        cnt += 1
print(cnt)
