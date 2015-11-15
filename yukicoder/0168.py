class UnionFind:

    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        group = []
        while self.table[x] >= 0:
            group.append(x)
            x = self.table[x]
        for g in group:
            self.table[g] = x
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


def distance2(px, py, qx, qy):
    return (px - qx) * (px - qx) + (py - qy) * (py - qy)


def acceptable(lenght):
    l = lenght * lenght
    uf = UnionFind(N)
    for i in range(N-1):
        for j in range(i+1,N):
            if D[i][j] <= l:
                uf.union(i, j)
    return uf.find(0) == uf.find(N - 1)


N = int(input())
P = []
for i in range(N):
    x, y = map(int, input().split())
    P.append((x, y))
D = [[0] * N for i in range(N)]
for i in range(N-1):
    for j in range(i+1,N):
        D[i][j] = distance2(P[i][0], P[i][1], P[j][0], P[j][1])
        D[j][i] = D[i][j]

lower_limit = 0
upper_limit = D[0][N-1]
while lower_limit < upper_limit:
    mid = (lower_limit + upper_limit) // 2
    if acceptable(mid):
        upper_limit = mid
    else:
        lower_limit = mid + 1
    # print(lower_limit, upper_limit)

if lower_limit % 10 > 0:
    lower_limit = lower_limit // 10 * 10 + 10
print(lower_limit)
