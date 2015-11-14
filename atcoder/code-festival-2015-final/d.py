class RMQ:

    def __init__(self, n_):
        self.n = 1
        while self.n < n_:
            self.n *= 2
        self.dat = [-1] * (2 * self.n - 1)

    def rec(self, a, b, k, l, r):
        if b <= l or r <= a:
            return float('-1')
        if a <= l and r <= b:
            return self.dat[k]
        else:
            rl = self.rec(a, b, 2 * k + 1, l, (l + r) // 2)
            rr = self.rec(a, b, 2 * k + 2, (l + r) // 2, r)
            return max(rl, rr)

    def update(self, k, a):
        reaf = k + self.n - 1
        self.dat[reaf] = a
        while reaf > 0:
            reaf = (reaf - 1) // 2
            self.dat[reaf] = max(self.dat[reaf * 2 + 1],
                                 self.dat[2 * reaf + 2])

    def query(self, a, b):
        return self.rec(a, b + 1, 0, 0, self.n)

N = int(input())
S = []
T = []
B = [0] * 100002
min_a = N
for i in range(N):
    s, t = map(int, input().split())
    S.append(s)
    T.append(t)
    B[s] += 1
    B[t] -= 1

A = [0] * 100002
for i in range(1, 100001):
    A[i] = A[i - 1] + B[i]

r = RMQ(100001)
# for i in range(100001):
for i in range(min(S),max(T)):
    r.update(i, A[i])

for i in range(N):
    max_a = max(r.query(0, S[i] - 1), r.query(S[i],T[i]-1) - 1, r.query(T[i], 100001))
    min_a = min(min_a, max_a)
print(min_a)
