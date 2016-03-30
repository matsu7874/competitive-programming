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

    def dist_kth_shortest_path(self,s,t,k):
        dist = self.min_dist_dijkstra(t)
        frontier = []
        frontier.append((dist[s],s,0,))
        cnt = 0
        while cnt < k:
            next_frontier = []
            cnt = 0
            for f,v,cost in frontier:
                if v == t:
                    next_frontier.append((f,v,cost))
                    cnt += 1
                else:
                    for e in self.graph[v]:
                        next_frontier.append((cost+e.cost+dist[e.target],e.target,cost+e.cost))
            next_frontier.sort()
            frontier = next_frontier[:k]
        print(frontier[k-1])

    def path_kth_shortest_path(self,s,t,k):
        dist = self.min_dist_dijkstra(t)
        frontier = []
        frontier.append((dist[s],s,0,[]))
        cnt = 0
        while cnt < k:
            next_frontier = []
            cnt = 0
            for f,v,cost,prev in frontier:
                if v == t:
                    if prev[-1] != t:
                        prev.append(t)
                    next_frontier.append((f,v,cost,prev))
                    cnt += 1
                else:
                    for e in self.graph[v]:
                        next_frontier.append((cost+e.cost+dist[e.target],e.target,cost+e.cost,prev+[v]))
            next_frontier.sort()
            frontier = next_frontier[:k]
        return frontier[:k]


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


if __name__ == '__main__':
    import random
    N=10
    g = Graph(N)
    for i in range(N):
        for j in range(4):
            g.add_bidirectional_edge(i,random.randint(0,N-1),random.randint(1,5))


    print(g.path_kth_shortest_path(0,N-1,3))
