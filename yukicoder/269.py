N,S,K = [int(x) for x in input().split()]
S -= K*N*(N-1)//2
if S<0:
    print(0)
    exit()
dp = [[0 for j in range(S+1)] for i in range(N+1)]
for i in range(0, S//N+1):
    dp[1][i*N] = 1
for i in range(2, N+1):
    t = N-i+1
    for j in range(S+1):
        dp[i][j] += dp[i-1][j]
        if j - t >= 0:
            dp[i][j] += dp[i][j-t]
print(dp[N][S] % 1000000007)
