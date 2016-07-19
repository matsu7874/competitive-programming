class SegmentTree():

    def __init__(self, size, initial=0):
        if isinstance(initial, list):
            node_size = 1
            size = len(initial)
            while node_size < size:
                node_size <<= 1
            self.st = [0] *(2*node_size-1)
            self.st[node_size-1:] = initial[:]
            
            i = node_size*2-2
            while i>1:
                self.st[i//2] = min(self.st[i-1],self.st[i])
                i -= 2
            self.size = node_size

        else:
            node_size = 1
            while node_size < size:
                node_size <<= 1
            self.st = [initial]*(2*node_size-1)
            self.size = node_size

    def update(self, target, new_value):
        target += self.size - 1
        self.st[target] = a
        while target > 0:
            target = (target - 1) // 2
            self.st[target] = min(self.st[target * 2 + 1],
                                  self.st[target * 2 + 2])

    #[a,b)の最小値を求める。RMQを解く。
    def query_value(self, a, b):
        return self._query_value(a, b, 0, 0, self.size)

    def _query_value(self, a, b, k, l, r):
        if r <= a or b <= l:
            return float('inf')
        if a <= l and r <= b:
            return self.st[k]
        vl = self._query_value(a, b, k * 2 + 1, l, (l + r) // 2)
        vr = self._query_value(a, b, k * 2 + 2, (l + r) // 2, r)
        return min(vl, vr)