import random


def create_unweighted_graph(V, E):
    total = 0
    nodes = [[] for i in range(V)]
    while total < E:
        s = random.randint(0, V - 1)
        t = random.randint(0, V - 1)
        if s == t:
            continue
        if t not in nodes[s]:
            nodes[s].append(t)
            total += 1
    edges = []
    for i in range(V):
        for t in nodes[i]:
            edges.append((i, t))
    return edges


def create_weighted_graph(V, E, costmax):
    total = 0
    nodes = [[] for i in range(V)]
    weight = [[] for i in range(V)]
    while total < E:
        s = random.randint(0, V - 1)
        t = random.randint(0, V - 1)
        if s == t:
            continue
        if t not in nodes[s]:
            nodes[s].append(t)
            weight[s].append(random.randint(1,costmax))
            total += 1
    edges = []
    for i in range(V):
        for j in range(len(nodes[i])):
            edges.append((i, nodes[i][j], weight[i][j]))
    return edges

if __name__ == '__main__':
    V = 10
    E = 30
    edges = create_weighted_graph(V, E,10)
    edges.sort()
    print(V, E)
    for e in edges:
        print(*e)
