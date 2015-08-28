N = int(input())
V = list(map(int, input().split()))
dp = [[0 for j in range(2)] for i in range(N)]
dp[0][1] = V[0]
for i in range(1, N):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + V[i]

print(max(dp[N - 1]))
