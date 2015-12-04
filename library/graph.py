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

    def min_dist_dijkstra(self, s):
        dist = [float('inf')] * self.size
        dist[s] = 0
        q = [(0, s)]
        while q:
            node = self.Node(*heapq.heappop(q))
            v = node.id
            if dist[v] < node.dist:
                continue
            for e in self.graph[v]:
                if dist[e.target] > dist[v] + e.cost:
                    dist[e.target] = dist[v] + e.cost
                    heapq.heappush(q, (dist[e.target], e.target))
        return dist

    def min_path_dijkstra(self, s, t):
        dist = [float('inf')] * self.size
        prev = [-1] * self.size
        dist[s] = 0
        q = [(0, s)]
        while q:
            node = self.Node(*heapq.heappop(q))
            v = node.id
            if dist[v] < node.dist:
                continue
            for e in self.graph[v]:
                if dist[e.target] > dist[v] + e.cost:
                    dist[e.target] = dist[v] + e.cost
                    heapq.heappush(q, (dist[e.target], e.target))
                    prev[e.target] = v
            if v == t:
                break

        path = [t]
        while path[-1] > -1:
            path.append(prev[path[-1]])
        return path[1:]

    def min_dist_queue(self, s):
        dist = [float('inf')] * self.size
        dist[s] = 0
        q = collections.deque()
        q.append(s)
        while q:
            v = q.popleft()
            for e in self.graph[v]:
                if dist[e.target] > dist[v] + e.cost:
                    dist[e.target] = dist[v] + e.cost
                    if e.cost == 0:
                        q.appendleft(e.target)
                    else:
                        q.append(e.target)
        return dist

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

        def __init__(self, dist, i):
            self.dist = dist
            self.id = i

        def __cmp__(self, other):
            if self.dist < other.dist:
                return -1
            elif self.dist == other.dist:
                return 0
            else:
                return 1
