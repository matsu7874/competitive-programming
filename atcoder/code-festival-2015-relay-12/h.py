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
        dist = [float('inf')]*self.size
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

    def min_dist_queue(self,s):
        dist = [float('inf')]*self.size
        dist[s] = 0
        q = collections.deque()
        q.append(s)
        while q:
            v = q.popleft()
            for e in self.graph[v]:
                if dist[e.target] > dist[v] + e.cost:
                    dist[e.target] = dist[v] + e.cost
                    if e.cost==0:
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

H, W = map(int, input().split())
C = [input() for i in range(H)]
g = Graph(H*W)
for i in range(H):
    for j in range(W):
        if i>0:
            g.add_edge(i*W+j,(i-1)*W+j,int(C[i][j]!=C[i-1][j]))
        if i<H-1:
            g.add_edge(i*W+j,(i+1)*W+j,int(C[i][j]!=C[i+1][j]))
        if j>0:
            g.add_edge(i*W+j,i*W+j-1,int(C[i][j]!=C[i][j-1]))
        if j<W-1:
            g.add_edge(i*W+j,i*W+j+1,int(C[i][j]!=C[i][j+1]))
        if i>0:
            g.add_edge(i*W+j,(i-1)*W+j,int(C[i][j]!=C[i-1][j]))
print(g.min_dist_queue(0)[W*H-1])
