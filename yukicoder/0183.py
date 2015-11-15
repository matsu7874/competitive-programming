N = int(input())
A = list(map(int, input().split()))
A.sort()
max_v = 2**15
dp = [False] * max_v
dp[0] = True
for i in range(N):
    dp2=dp[:]
    print(dp[:5])
    for j in range(max_v):
        if dp[j]:
            dp2[i ^ j] = True
    dp = dp2[:]
print(dp.count(True))
