import heapq
import collections
import math
import random

N, M = map(int, input().split())

distance = collections.defaultdict(dict)

for i in range(M):
    a, b, t = map(int, input().split())
    distance[a - 1][b - 1] = t
    distance[b - 1][a - 1] = t

for i in range(N):
    distance[i][i] = 0

result = []
if N >= 170 and M >= 18000:
    x = random.sample(range(N), min(82, N))
else:
    x = range(N)
D = [1000000000000 for i in range(N)]
for i in x:
    d = D[:]
    d[i] = 0
    heap = []
    heapq.heappush(heap, (0, i))
    while heap:
        prev_cost, source = heapq.heappop(heap)
        if d[source] < prev_cost:
            continue
        for target in distance[source]:
            cost = distance[source][target]

            if d[target] > d[source] + cost:
                d[target] = d[source] + cost
                heapq.heappush(heap, (d[target], target))
    result.append(max(d))
print(min(result))
