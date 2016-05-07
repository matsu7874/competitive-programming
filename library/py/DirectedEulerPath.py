import heapq
import collections


class Graph:

    def __init__(self, size):
        self.size = size
        self.graph = [[] for i in range(size)]

    def add_edge(self, source, target, cost):
        self.graph[source].append(self.Edge(target, cost))

    def add_bidirectional_edge(self, source, target, cost):
        self.add_edge(source, target, cost)
        self.add_edge(target, source, cost)

    def is_connected(self):
        visited = [False for i in range(self.size)]
        

    def euler_path(self, source):
        def dfs(g, a, route):
            while g.graph[a]:
                b = g.graph[a].pop()
                dfs(g, b, route)
            route.append(a)

        deg = [0 for i in range(self.size)]
        used_edge = 0
        for i in range(self.size):
            used_edge += len(self.graph[i])
            for j in range(len(self.graph[i])):
                deg[self.graph[i][j].target] -= 1
            deg[i] += len(self.graph[i])
        route = []
        nonzero = self.size - deg.count(0)
        if nonzero == 0 or (nonzero == 2 and deg[source] == 1):
            g_ = Graph(self.size, self.graph)
            self.dfs(g_, source, route)
        if len(route) != used_edge + 1:
            route = []
        route.reverse()
        return route

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
    n, m = map(int, input().split())
    g = Graph(n)
    for i in range(m):
        s, t, c = map(int, input().split())
        g.add_edge(s, t, c)
    path = g.euler_path(0)
