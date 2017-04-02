import collections
N,M = map(int, input().split())

nodes = [collections.defaultdict(int) for i in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    nodes[a-1][b-1] = 1
    nodes[b-1][a-1] = 1


shots = []
Q = int(input())
for i in range(Q):
    v,d,c = map(int, input().split())
    shots.append((v-1, d, c))
alive = [True for i in range(N)]
colors = [0 for i in range(N)]
sizes = [-1 for i in range(N)]
for query in range(Q-1, -1, -1):
    v, d, c = shots[query]
    dq = collections.deque()
    dq.append((d, v))
    visited = [False for i in range(N)]
    while dq:
        print(dq)
        size, idx = dq.popleft()
        if sizes[idx] >= size:
            continue
        else:
            sizes[idx] = size
        visited[idx] = True
        if colors[idx] == 0:
            colors[idx] = c
        for nv, nd in nodes[idx].items():
            if not visited[nv] and size-nd >= 0:
                dq.append((size-nd, nv))
        
        len_next_nodes = len(nodes[idx])
        if len_next_nodes >= 150 or not alive[idx]:
            continue
        alive[idx] = False
        for nvi, ndi in nodes[idx].items():
            nodes[nvi].pop(idx)
            for nvj, ndj in nodes[idx].items():
                if nvi >= nvj:
                    continue
                if nvj in nodes[nvi]:
                    nodes[nvi][nvj] = nodes[nvj][nvi] = min(nodes[nvi][nvj], ndi + ndj)
                else:
                    nodes[nvi][nvj] = nodes[nvj][nvi] = ndi + ndj


print(*colors, sep='\n')
