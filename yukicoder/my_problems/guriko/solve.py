import decimal
N = int(input())
S = [int(x) for x in input().split()]
AR, AS = [decimal.Decimal(x) for x in input().split()]
BR, BS = [decimal.Decimal(x) for x in input().split()]
steps = [(3,0),(6,0),(0,3),(0,6)]
AP = decimal.Decimal(1-AR-AS)
BP = decimal.Decimal(1-BR-BS)
draw = decimal.Decimal(AR*BR + AS*BS + AP*BP)
P = [decimal.Decimal((AR*BS)/(1-draw)), decimal.Decimal((AS*BP+AP*BR)/(1-draw)), decimal.Decimal((AS*BR)/(1-draw)), decimal.Decimal((AP*BS+AR*BP)/(1-draw))]

dp = [[decimal.Decimal('0.0') for j in range(N+6)] for i in range(N+6)]
dp[S[0]][S[1]] = 1.0
for i in range(S[0], N, 3):
    for j in range(S[1], N, 3):
        for k in range(4):
            dp[i+steps[k][0]][j+steps[k][1]] += decimal.Decimal(P[k])*decimal.Decimal(dp[i][j])
win_rate = 0
for i in range(N, N+6):
    for j in range(S[1], N, 3):
        win_rate += dp[i][j]
print(str(win_rate))
