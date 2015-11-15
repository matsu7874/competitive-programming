import heapq

N = int(input())
p = []
for i in range(N):
    s, c = map(int, input().split())
    heapq.heappush(p,(i,s,c))
while p:
    q = heapq.heappop(p)
    
