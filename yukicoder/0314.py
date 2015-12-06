N = int(input())
if N == 1:
    print(1)
    exit()

dp = [0] * (N + 2)
dp[0] = 1
dp[1] = 1
dp[2] = 0

for i in range(1, N + 2):
    dp[i] = (dp[i - 2] + dp[i - 3]) % 1000000007
print((dp[N] + dp[N - 1] + dp[N - 2]) % 1000000007)
