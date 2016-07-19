class SegmentTree():

    def __init__(self, size, initial=0):
        if isinstance(initial, list):
            node_size = 1
            size = len(initial)
            while node_size < size:
                node_size <<= 1
            self.st = [(float('inf'), float('inf'))] * (2 * node_size - 1)
            for i in range(size):
                self.st[node_size - 1 + i] = (initial[i], i)
            i = node_size * 2 - 2
            while i > 1:
                self.st[(i - 1) // 2] = min(self.st[i - 1], self.st[i])
                i -= 2
            self.size = node_size

        else:
            node_size = 1
            while node_size < size:
                node_size <<= 1
            self.st = [initial] * (2 * node_size - 1)
            self.size = node_size

    def update(self, target, new_value):
        target += self.size - 1
        self.st[target] = a
        while target > 0:
            target = (target - 1) // 2
            self.st[target] = min(self.st[target * 2 + 1],
                                  self.st[target * 2 + 2])

    #[a,b)の最小値を求める。RMQを解く。
    def query(self, a, b):
        return self._query(a, b, 0, 0, self.size)

    def _query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return (float('inf'), -1)
        if a <= l and r <= b:
            return self.st[k]
        vl = self._query(a, b, k * 2 + 1, l, (l + r) // 2)
        vr = self._query(a, b, k * 2 + 2, (l + r) // 2, r)
        return min(vl, vr)


class Tree():

    def __init__(self, size):
        self.size = size
        self.edges = [[] for i in range(size)]

    def create_nodes(self, s, t):
        self.edges[s].append(t)

    def create_nodes_bidirectional(self, s, t):
        self.edges[s].append(t)
        self.edges[t].append(s)

    def build(self, cost, root=0):
        self.route = []
        depth = [0] * self.size
        visited = [False] * self.size
        self.cost = [0] * self.size
        self.cost[root] = cost[root]
        cur = root
        d = 0
        c = cost[root]
        stack = []
        while True:
            self.route.append(cur)
            depth[cur] = d
            self.cost[cur] = c
            visited[cur] = True
            stack.append(cur)
            for child in self.edges[cur]:
                if visited[child]:
                    continue
                cur = child
                break
            if cur == stack[-1]:
                c -= cost[cur]
                stack.pop()
                d -= 1
                if stack:
                    cur = stack.pop()
                else:
                    break
            else:
                c += cost[cur]
                d += 1

        route_depth = [depth[self.route[i]] for i in range(len(self.route))]
        self.rmq = SegmentTree(self.size, initial=route_depth)
        self.first_occur = [-1] * self.size
        for i in range(len(self.route)):
            if self.first_occur[self.route[i]] == -1:
                self.first_occur[self.route[i]] = i

    def query(self, a, b):
        first = min(self.first_occur[a], self.first_occur[b])
        second = max(self.first_occur[a], self.first_occur[b])
        min_v, min_i = self.rmq.query(first, second)
        return self.route[min_i]


n = int(input())
tree = Tree(n)
for i in range(n - 1):
    a, b = map(int, input().split())
    tree.create_nodes_bidirectional(a, b)

tariff = [0] * n
for i in range(n):
    tariff[i] = int(input())
tree.build(tariff)

total = 0
m = int(input())
memo = {}
for i in range(m):
    a, b, c = map(int, input().split())
    if a > b:
        a, b = b, a
    if (a, b) in memo:
        total += memo[(a, b)] * c
    else:
        lca = tree.query(a, b)
        memo[(a, b)] = tree.cost[a] + tree.cost[b] - \
            2 * tree.cost[lca] + tariff[lca]
        total += memo[(a, b)] * c
print(total)
