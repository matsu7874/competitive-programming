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

if __name__ == '__main__':
    n = int(input())
    tree = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
    a, b = search_diameter_nodes(tree)
    print(a + 1, b + 1)
