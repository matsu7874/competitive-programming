import math
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    log = math.log10(A) * B
    Z = int(log)
    xy = log - Z
    l = 0.0
    r = 10.0
    while l + 0.0001 < r:
        m = (l + r) / 2
        t = math.log10(m)
        if t < xy:
            l = m
        elif xy <= t:
            r = m
    X = int(l)
    Y = int((l - X) * 10)
    if X==0:
        X=1
        Y=0
    print(X, Y, Z)
