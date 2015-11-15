N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=list(map(int, input().split()))
cost = [[0],[0]]
for i in range(N-1):
    cost[0].append(cost[0][i]+A[i])
    cost[1].append(cost[1][i]+B[N-2-i])
cost[1].reverse()
min_cost = 99999999999
min_i=-1
for i in range(N):
    if min_cost > cost[0][i]+cost[1][i]+C[i]:
        min_cost = cost[0][i]+cost[1][i]+C[i]
        min_i = i
min_cost2 = 99999999999
for i in range(N):
    if min_cost2 > cost[0][i]+cost[1][i]+C[i] and i!=min_i:
        min_cost2 = cost[0][i]+cost[1][i]+C[i]

print(min_cost+min_cost2)
