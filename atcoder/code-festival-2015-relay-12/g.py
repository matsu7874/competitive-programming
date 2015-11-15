N, M, L = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
C = []
D = []
for i in range(M):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

dp = [0 for j in range(L + 1)]
for i in range(M):
    for j in range(L,-1,-1):
        if j >= C[i]:
            dp[j] = max(dp[j], dp[j - C[i]] + D[i])

max_value = 0
for i in range(N):
    if L - A[i] > 0:
        max_value = max(max_value, B[i] + dp[L - A[i]])
print(max_value)
