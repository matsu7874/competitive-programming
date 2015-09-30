N = int(input())
d = [0] * 6
for i in range(N):
    a, b = map(float, input().split())
    if a >= 35:
        d[0] += 1
    elif a >= 30:
        d[1] += 1
    elif a >= 25:
        d[2] += 1
    if b >= 25:
        d[3] += 1
    if a >= 0 and b < 0:
        d[4] += 1
    if a < 0:
        d[5] += 1
print(*d)
