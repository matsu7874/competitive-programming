class UnionFind:

    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] >= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
        return self.table[s1]

N, Q = map(int, input().split())
uf = UnionFind(N + 1)
for _ in range(Q):
    a, b, c = map(int, input().split())
    if a == 0:
        uf.union(b, c)
    elif a == 1:
        if uf.find(b) == uf.find(c):
            print('YES')
        else:
            print('NO')
