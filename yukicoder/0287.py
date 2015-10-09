N = int(input())

dp = [[0 for j in range(600 + 1)] for i in range(8 + 1)]
dp[0][0] = 1
for i in range(8):
    for j in range(6 * N + 1):
        for k in range(N + 1):
            if j + k <= 6 * N:
                dp[i + 1][j + k] += dp[i][j]
print(dp[8][6 * N])
