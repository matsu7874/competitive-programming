def combination(n, r, limit):
    res = 1
    t = r - 1
    while t >= 0 and res <= limit:
        res = res * (n - t) // (r - t)
        t -= 1
    return res

q = int(input())
for _ in range(q):
    d, x, t = map(int, input().split())
        program = combination(d + x - 1, d - 1, t)
    if program > t:
        print('ZETUBOU')
    else:
        print('AC')
