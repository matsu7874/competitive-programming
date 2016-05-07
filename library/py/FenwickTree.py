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
