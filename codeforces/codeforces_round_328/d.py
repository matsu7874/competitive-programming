n, m = map(int, input().split())
A = list(map(int, input().split()))
X = set([0])
Y = set(A)
adj = [[float('inf') for j in range(n)] for i in range(n)]
cost = 0
edges = []

while len(Y) != 0:
    mcost = float('inf')
    edge = None
    for ex in X:
        for ey in Y:
            if mcost > adj[x][y]:
                mcost = adj[x][y]
                edge = [x, y]
    X.add(edge[1])
    Y.remove(edge[1])
    edges.append(edge)

print()
