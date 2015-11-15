N = int(input())
l = 0
r = 10**18
for loop in range(200):
    m = (l + r) / 2
    dp = [0] * (N+1)
    for i in range(1, N + 1):
        for j in range(1, 6 + 1):
            if j > i:
                dp[i] += m
            if i > j:
                dp[i] += dp[i - j]
        dp[i] = dp[i] / 6 + 1
    if dp[N] >= m:
        l = m
    else:
        r = m
print((l + r) / 2)
