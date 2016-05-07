# export complement graph
# directed graph

def complement_graph(V,edges):
    nodes = [[] for i in range(V)]
    for e in edges:
        nodes[e[0]].append(e[1])
    complement_edges = []
    for i in range(V):
        for j in range(V):
            if i == j:
                continue
            if j not in nodes[i]:
                complement_edges.append((i,j))
    return complement_edges

if __name__ == '__main__':
    V, E = map(int, input().split())
    edges = []
    for i in range(E):
        s, t, d = map(int, input().split())
        edges.append((s, t, d))
    complement = complement_graph(V,edges)
    e = len(complement)
    print(V,e)
    for i in range(e):
        print(*complement[i])
