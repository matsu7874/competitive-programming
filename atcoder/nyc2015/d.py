ZERO = 100
NUMBER = 301

n = int(input())
cost = [[999999 for j in range(NUMBER)] for i in range(NUMBER)]
for i in range(NUMBER):
    cost[i][i] = 0
for _ in range(n):
    a = int(input())+ZERO
    for i in range(a):
        if 2*a-i<NUMBER:
            cost[i][2*a-i] = 1
            cost[2*a-i][i] = 1

for k in range(NUMBER):
    for i in range(NUMBER):
        for j in range(NUMBER):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

q = int(input())
for _ in range(q):
    (s, t) = [int(x)+ZERO for x in input().split()]
    if cost[s][t] >= 999999:
        print(-1)
    else:
        print(cost[s][t])
