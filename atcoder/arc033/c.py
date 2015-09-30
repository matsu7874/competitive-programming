import heapq
Q=int(input())
h = []
for i in range(Q):
    t,x=map(int, input().split())
    if t == 1:
        heapq.heappush(h,x)
    else:
        print(heapq.heappop(h))
