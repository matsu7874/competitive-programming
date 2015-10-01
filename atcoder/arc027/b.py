class UnionFind:

    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        # 集合の代表を求める
        while self.table[x] >= 0:
            x = self.table[x]
        return x

    def union(self, x, y):
        # 併合
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

    def get_table(self):
        return list(self.table)


def idx(c):
    if c in '0123456789':
        return int(c)
    else:
        return 10 + ord(c) - ord('A')

N = int(input())
s1 = input()
s2 = input()
uf = UnionFind(36)
for i in range(N):
    uf.union(idx(s1[i]), idx(s2[i]))

total = 1
checked = [False] * 36
for i in range(N):
    if not checked[idx(s1[i])] and not checked[idx(s2[i])]:
        if i == 0:
            cnt = 9
        else:
            cnt = 10
        for j in range(10):
            if uf.find(j) == uf.find(idx(s1[i])):
                cnt = 1
                break
        total *= cnt
        checked[idx(s1[i])] = True
        checked[idx(s2[i])] = True
print(total)
