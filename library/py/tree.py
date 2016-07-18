def search_farthest_node(tree, source):
    size = len(tree)
    visited = [False] * size
    distance = [-1] * size
    distance[source] = 0
    farthest_node = (-1, -1)
    queue = [source]
    while queue:
        node = queue.pop()
        visited[node] = True
        if distance[node] > farthest_node[1]:
            farthest_node = (node, distance[node])
        for next in tree[node]:
            if visited[next]:
                continue
            distance[next] = distance[node] + 1
            queue.append(next)
    return farthest_node[0]


def search_diameter_nodes(tree):
    a = search_farthest_node(tree, 0)
    b = search_farthest_node(tree, a)
    return (a, b)
