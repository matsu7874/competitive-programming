RANGE = 10001
ZERO = 5001
N = int(input())
W = [int(x) for x in input().split()]
dp = [[False for j in range(RANGE)] for i in range(N+1)]
dp[0][ZERO] = True
for i in range(N):
    for j in range(RANGE):
        if dp[i][j] == True:
            if j + W[i] < RANGE:
                dp[i+1][j+W[i]] = True
            if 0 <= j - W[i]:
                dp[i+1][j-W[i]] = True
if dp[N][ZERO]:
    print('possible')
else:
    print('impossible')
