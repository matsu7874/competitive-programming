def prim(V, edges):
    import heapq
    E = len(edges)
    nodes = [[] for i in range(V)]
    cost = [[] for i in range(V)]
    for s, t, c in edges:
        nodes[s].append(t)
        cost[s].append(c)

    visited = [False] * V
    total = 0
    used_edges = []
    h = [(0, -1, 0)]
    while h:
        c, s, t = heapq.heappop(h)
        if visited[t]:
            continue
        total += c
        used_edges.append((c, s, t))
        visited[t] = True
        for i in range(len(nodes[t])):
            nv = nodes[t][i]
            if not visited[nv]:
                heapq.heappush(h, (cost[t][i], t, nv))
    print(total)
    return used_edges

if __name__ == '__main__':
    root = 0
    V, E = map(int, input().split())
    # V, E, root = map(int, input().split())
    edges = []
    for i in range(E):
        s, t, d = map(int, input().split())
        edges.append((s, t, d))
    st = prim(V, edges)
    st.sort()
    for e in st:
        print(*e)
