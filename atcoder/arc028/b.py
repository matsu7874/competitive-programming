import heapq
n, k = map(int, input().split())
a = list(map(int, input().split()))
youngers = [(-a[i], i + 1) for i in range(k)]
heapq.heapify(youngers)
for i in range(k, n):
    old, th = heapq.heappop(youngers)
    print(th)
    if -old < a[i]:
        heapq.heappush(youngers, (old, th))
    else:
        heapq.heappush(youngers, (-a[i], i + 1))
print(heapq.heappop(youngers)[1])
