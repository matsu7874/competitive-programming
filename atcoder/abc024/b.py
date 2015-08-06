n,t = [int(x) for x in input().split()]
open_time = 0
last = int(input())
for _ in range(n-1):
    tmp = int(input())
    if tmp-last > t:
        open_time += t
    else:
        open_time += tmp-last
    last = tmp
print(open_time+t)
