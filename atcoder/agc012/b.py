import collections
N,M = map(int, input().split())

nodes = [[] for i in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)


shots = []
Q = int(input())
for i in range(Q):
    v,d,c = map(int, input().split())
    shots.append((v-1, d, c))
colors = [0 for i in range(N)]
sizes = [0 for i in range(N)]
edges = [[i] for i in range(N)]
for i in range(Q-1, -1, -1):
    v, d, c = shots[i]
    if colors[v] == 0:
        colors[v] = c
        dq = collections.deque()

        for nv in nodes[v]:
            dq.append((1, nv))
        visited = [False for i in range(N)]
        visited[v] = True
        while dq:
            dist, idx = dq.popleft()
            visited[idx] = True
            if colors[idx] == 0:
                colors[idx] = c
            if dist >= d:
                continue
            for nv in nodes[idx]:
                if not visited[nv]:
                    dq.append((dist+1, nv))
print(*colors, sep='\n')
