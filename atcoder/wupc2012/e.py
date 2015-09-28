import heapq
import collections
N, M = map(int, input().split())
edges = collections.defaultdict(dict)
for i in range(N):
    edges[i][i] = 0
for i in range(M):
    f, t, c = map(int, input().split())
    if f==N-1:
        for j in range(28):
            edges[t * 28 + j][f * 28 + (j + c) % 28] = c
    elif t==N-1:
        for j in range(28):
            edges[f * 28 + j][t * 28 + (j + c) % 28] = c
    else:
        for j in range(28):
            edges[f * 28 + j][t * 28 + (j + c) % 28] = c
            edges[t * 28 + j][f * 28 + (j + c) % 28] = c
distance = [10000000000 for i in range(N * 28)]
distance[0] = 0
heap = [(0, 0)]
while heap:
    prev_cost, source = heapq.heappop(heap)
    if distance[source] < prev_cost:
        continue
    for target in edges[source]:
        cost = edges[source][target]
        if distance[target] > distance[source] + cost:
            distance[target] = distance[source] + cost
            heapq.heappush(heap, (distance[target], target))
ans = min(distance[(N - 1) * 28], distance[(N - 1) * 28 + 4],
          distance[(N - 1) * 28 + 7], distance[(N - 1) * 28 + 8],
          distance[(N - 1) * 28 + 12], distance[(N - 1) * 28 + 14],
          distance[(N - 1) * 28 + 16], distance[(N - 1) * 28 + 20],
          distance[(N - 1) * 28 + 21], distance[(N - 1) * 28 + 24])
print(ans)
