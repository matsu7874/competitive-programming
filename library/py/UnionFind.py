class UnionFind:

    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.size = size
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        # 集合の代表を求める
        while self.table[x] >= 0:
            if self.table[self.table[x]] >= 0:
                self.table[x] = self.table[self.table[x]]
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

    def count_group(self):
        count = 0
        for i in range(self.size):
            if self.table[i] < 0:
                count += 1
        return count
