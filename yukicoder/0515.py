class SegmentTree():

    def __init__(self, size, initial=0):
        if isinstance(initial, list):
            node_size = 1
            size = len(initial)
            while node_size < size:
                node_size <<= 1
            self.st = [0] * (2*node_size-1)
            self.st[node_size-1:] = initial[:]
            
            i = node_size*2-2
            print(node_size)
            while i>1:
                print(i, len(self.st))
                self.st[i//2] = min(self.st[i-1], self.st[i])
                i -= 2
            self.size = node_size

        else:
            node_size = 1
            while node_size < size:
                node_size <<= 1
            self.st = [initial]*(2*node_size-1)
            self.size = node_size

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

def next_query(n, x, d):
    i = (x // (n-1))
    j = (x % (n-1))
    if i > j:
        i, j = j, i
    else:
        j += 1
    x = (x+d) % (n * (n-1))
    return i, j, x

def lcp(a,b):
    size_a =  len(a)
    size_b =  len(b)
    size = min(size_a, size_b)
    for i in range(size):
        if a[i] != b[i]:
            return i
    return size


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append((input().strip(), i))
    s.sort()
    idx = [0] + [i for i in range(n)] + [0]
    for i in range(n):
        idx[s[i][1]] = i
    
    diff = [lcp(s[i][0], s[i+1][0]) for i in range(n-1)]
    st = SegmentTree(n, diff)


    m, x, d = map(int, input().split())
    total = 0
    for _ in range(min(m, n*(n+1))):
        i, j, x = next_query(n, x, d)
        total += st.query_value(i, j)
    if m <= n*(n+1):
        print(total)
        exit()
    
    total *= m // (n*(n+1))
    for _ in range(m % (n*(n+1))):
        i, j, x = st.query_value(i, j)
        total += lcp(s[i], s[j])

    print(total)

if __name__ == '__main__':
    main()
