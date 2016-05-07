# directed graph
# weighted graph


def dijkstra(V, edges, root):
    import heapq

    visited = [False] * V
    nodes = [[] for i in range(V)]
    cost = [[] for i in range(V)]

    for e in edges:
        s, t, d = e
        nodes[s].append(t)
        cost[s].append(d)

    dist = [float('inf')] * V
    dist[root] = 0

    h = [(0, root)]
    while h:
        c, v = heapq.heappop(h)
        if visited[v]:
            continue
        visited[v] = True
        for i in range(len(nodes[v])):
            t = nodes[v][i]
            nc = c + cost[v][i]
            if dist[t] > nc:
                dist[t] = nc
                heapq.heappush(h, (nc, t))
    return dist


def dijkstra_path(V, edges, source, target):
    import heapq

    visited = [False] * V
    nodes = [[] for i in range(V)]
    cost = [[] for i in range(V)]
    prev = [-1 for i in range(V)]

    for e in edges:
        s, t, d = e
        nodes[s].append(t)
        cost[s].append(d)

    dist = [float('inf')] * V
    dist[source] = 0

    h = [(0, root)]
    while h:
        c, v = heapq.heappop(h)
        if visited[v]:
            continue
        visited[v] = True
        for i in range(len(nodes[v])):
            t = nodes[v][i]
            nc = c + cost[v][i]
            if dist[t] > nc:
                dist[t] = nc
                heapq.heappush(h, (nc, t))
                prev[t] = v
    path = [target]
    while path[-1] != source and path[-1] != -1:
        path.append(prev[path[-1]])
    return (path[-1] == source, path[::-1])


if __name__ == '__main__':
    root = 0
    V, E = map(int, input().split())
    # V, E, root = map(int, input().split())
    edges = []
    for i in range(E):
        s, t, d = map(int, input().split())
        edges.append((s, t, d))
    dist = dijkstra(V, edges, root)
    for i in range(V):
        if dist[i] == float('inf'):
            print('INF')
            print(dijkstra_path(V, edges, root, i))
        else:
            print(dist[i])
            print(dijkstra_path(V, edges, root, i))
