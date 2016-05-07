class FenwickTree:

    def __init__(self, n):
        self.size = n
        self.tree = [0] * self.size

    def add(self, index, value):
        x = index
        while x < self.size:
            self.tree[x] += value
            x |= x + 1

    def sum(self, index):
        # 半開区間[0,index)
        ret = 0
        x = index - 1
        while x >= 0:
            ret += self.tree[x]
            x = (x & (x + 1)) - 1
        return ret

n = 200000 + 1
ft = FenwickTree(n)
q = int(input())
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        ft.add(x, 1)
    else:
        l = 0
        r = n
        while l + 1 < r:
            m = (l + r) // 2
            rank = ft.sum(m) + 1
            if rank <= x:
                l = m
            else:
                r = m
        print(l)
        ft.add(l, -1)
