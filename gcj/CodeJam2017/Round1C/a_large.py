import math
import heapq
def solve(n, k, c):
    maxs = 0
    for i in range(n-k+1):
        s = 0
        s += c[i][0]**2 * math.pi
        s += c[i][1]
        h = []
        for j in range(i+1, n):
            heapq.heappush(h, -c[j][1])
        for j in range(k-1):
            s += -heapq.heappop(h)
        maxs = max(maxs, s)
    return maxs

def print_answer(t, ans):
    tmpl = 'Case #{0}: {1}'
    print(tmpl.format(t+1, ans))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N,K = map(int, input().split())
        C = []
        for i in range(N):
            r, h = map(int, input().split())
            C.append((r, 2*r*h*math.pi))
        C.sort(reverse=True)
        ans = solve(N,K,C)
        print_answer(_, ans)
