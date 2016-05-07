class Graph:

    def __init__(self, size):
        self.size = size
        self.graph = [[] for i in range(size)]

    def add_edge(self, source, target, cost):
        self.graph[source].append(self.Edge(target, cost))

    def add_bidirectional_edge(self, source, target, cost):
        self.add_edge(source, target, cost)
        self.add_edge(target, source, cost)

    def __str__(self):
        res = ''
        for i in range(self.size):
            res += str(i)
            for e in self.graph[i]:
                res += ' ' + str(e.target)
            res += '\n'
        return res

    class Edge:

        def __init__(self, target, cost):
            self.target = target
            self.cost = cost

    class Node:

        def __init__(self, cost, i):
            self.cost = cost
            self.id = i

        def __cmp__(self, other):
            if self.cost < other.cost:
                return -1
            elif self.cost == other.cost:
                return 0
            else:
                return 1


if __name__ == '__main__':
    g = Graph(10)
    g.add_bidirectional_edge(0,1,2)
    g.add_bidirectional_edge(4,1,2)
    g.add_bidirectional_edge(6,3,2)
    g.add_edge(9,7,8)
    g.add_edge(9,8,3)
    g.add_edge(4,5,3)
    print(g)
