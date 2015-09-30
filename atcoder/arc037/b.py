N, M = map(int, input().split())
adj = [[] for i in range(N)]
visited = [False] * N

for i in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)

cnt = 0
queue = []
i = 0
is_tree = True
while i < N:
    if not queue:
        queue.append((i, -1))
        is_tree = True
    while queue:
        v, prev = queue.pop()
        visited[v] = True
        for next_v in adj[v]:
            if next_v == prev:
                continue
            if visited[next_v]:
                is_tree = False
            else:
                visited[next_v] = True
                queue.append((next_v, v))
    while i < N and visited[i]:
        i += 1
    if is_tree:
        cnt += 1
print(cnt)
