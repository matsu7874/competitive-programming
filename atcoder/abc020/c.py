import heapq
h, w, t = map(int, input().split())
s = [input() for i in range(h)]
sy = 0
sx = 0
gy = 0
gx = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == 'S':
            sy = i
            sx = j
        elif s[i][j] == 'G':
            gy = i
            gx = j

sb = 1
lb = t + 1
nodes = [[] for i in range(w * h)]
costs = [[] for i in range(w * h)]
for i in range(h):
    for j in range(w - 1):
        nodes[i * w + j].append(i * w + j + 1)
        costs[i * w + j].append(2 if s[i][j + 1] == '#' else 1)
    for j in range(1, w):
        nodes[i * w + j].append(i * w + j - 1)
        costs[i * w + j].append(2 if s[i][j - 1] == '#' else 1)
for i in range(h - 1):
    for j in range(w):
        nodes[i * w + j].append(i * w + j + w)
        costs[i * w + j].append(2 if s[i + 1][j] == '#' else 1)
for i in range(1, h):
    for j in range(w):
        nodes[i * w + j].append(i * w + j - w)
        costs[i * w + j].append(2 if s[i - 1][j] == '#' else 1)

while sb + 1 < lb:
    m = (sb + lb) // 2
    for i in range(w * h):
        for j in range(len(costs[i])):
            if costs[i][j] > 1:
                costs[i][j] = m
    accessible = False
    visited = [False] * w * h
    dist = [float('inf')] * w * h
    dist[sy * w + sx] = 0

    hq = [(0, sy * w + sx)]
    while hq:
        c, v = heapq.heappop(hq)
        if v == gy * w + gx:
            accessible = True
            break
        if visited[v]:
            continue
        visited[v] = True
        for i in range(len(nodes[v])):
            target = nodes[v][i]
            nc = c + costs[v][i]
            if dist[target] > nc and nc <= t:
                dist[target] = nc
                heapq.heappush(hq, (nc, target))
    if accessible:
        sb = m
    else:
        lb = m
print(sb)
