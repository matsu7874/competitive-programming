INF = float('inf')
W = int(input())
N, K = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
dp = [[INF for j in range(K * 100 + 1)] for i in range(K + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(K, 0, -1):
        for k in range(B[i], K * 100 + 1):
            if dp[j - 1][k - B[i]] == INF:
                continue
            dp[j][k] = min(dp[j][k], dp[j - 1][k - B[i]] + A[i])

for i in range(K * 100, 0, -1):
    for j in range(K + 1):
        if dp[j][i] <= W:
            print(i)
            exit()
print(0)
