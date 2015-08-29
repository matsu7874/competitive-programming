import heapq

N, M = map(int, input().split())

E = []
for i in range(M):
    a, b, t = map(int, input().split())
    E.append((a - 1, b - 1, t))
inf = 1000 * N
shortest_worst_time = inf

distance = [[inf for j in range(N)] for i in range(N)]
for i in range(N):
    distance[i][i] = 0
for e in E:
    distance[e[0]][e[1]] = e[2]
    distance[e[1]][e[0]] = e[2]

for i in range(N):
    d = [inf for i in range(N)]
    d[i] = 0
    Q = []
    heapq.heappush(Q, (d[i], i))
    while len(Q) > 0:
        prev_cost, source = heapq.heappop(Q)
        if d[source] < prev_cost:
            continue
        for target in range(N):
            cost = distance[source][target]
            if d[target] > d[source] + cost:
                d[target] = d[source] + cost
                heapq.heappush(Q, (d[target], target))
    shortest_worst_time = min(shortest_worst_time, max(d))
    for j in range(N):
        distance[i][j] = d[j]
        distance[j][i] = d[j]
print(shortest_worst_time)
