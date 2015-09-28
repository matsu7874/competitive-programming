from collections import namedtuple
from heapq import heappush, heappop

class P(tuple):
    __lt__ = lambda self, other: not super().__lt__(other)

N, M = map(int, input().strip().split())

D = [-1, 1, -(M + 2), M + 2]

C = ''.join(
    ['#' * (M + 2)] +
    ['#' + input().strip() + '#' for _ in range(N)] +
    ['#' * (M + 2)])

SP = C.find('g')

memo = [0 for _ in C]

h = [P((10.0, SP))]

while len(h) > 0:
    b, p = heappop(h)

    for d in D:
        p_ = p + d
        l = C[p_]

        if l == 's':
            print(b * 0.99)
            exit(0)

        if l == '#' or l == 'g':
            continue

        b_ = min(float(l), b * 0.99)

        if b_ > memo[p_]:
            memo[p_] = b_
            heappush(h, P((b_, p_)))

print(-1)
