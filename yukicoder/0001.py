N = int(input())
C = int(input())
V = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
Y = list(map(int, input().split()))
M = list(map(int, input().split()))

Vec = [(S[i], T[i], Y[i], M[i]) for i in range(V)]
Vec.sort()

dp = [[50001 for j in range(601)] for i in range(51)]
dp[1][C] = 0
for v in Vec:
    for i in range(C + 1):
        dp[v[1]][i] = min(dp[v[1]][i], dp[v[0]][i + v[2]] + v[3])
min_minute = min(dp[N])
if min_minute == 50001:
    print(-1)
else:
    print(min_minute)
