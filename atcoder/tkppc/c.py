N,M = [int(x) for x in input().split()]
S = int(input())
D = [(0,0), (S,0)]
for i in range(N):
    t,k = [int(x) for x in input().split()]
    D.append((t,k))
D.sort()
k_now = 0
t_total = 0
t_now = 0
for i in range(N+2):
    if k_now >= M:
        t_total += D[i][0] - t_now
    t_now = D[i][0]
    k_now += D[i][1]
print(t_total)
