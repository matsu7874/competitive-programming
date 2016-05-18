n = int(input())
balloons = []
for i in range(n):
    h, s = map(int, input().split())
    balloons.append((h, s))
l = 0
r = 10**15
while l + 1 < r:
    m = (l + r) // 2
    gettable = True
    queue = []
    for i in range(n):
        h = balloons[i][0]
        s = balloons[i][1]
        queue.append(((m - h) / s, h, s))
    queue.sort()

    for i in range(n):
        if m < queue[i][1] + queue[i][2] * i:
            gettable = False
            break
    if gettable:
        r = m
    else:
        l = m
print(r)
