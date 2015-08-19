import heapq
N = int(input())
A = list(map(int, input().split()))
A.sort()
B = [int(x)//2 for x in input().split()]*2
H = [(a,0) for a in A]

min_max_cnt = N
for i in range(N):
    h = H[:]
    for b in B[i:i+N]:
        s,t = h[0]
        heapq.heapreplace(h, (b+s, t+1))
    max_cnt = max(t for s,t in h)
    if min_max_cnt > max_cnt:
        min_max_cnt = max_cnt

print(min_max_cnt)
