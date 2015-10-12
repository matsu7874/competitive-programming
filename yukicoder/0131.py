x, y, d = map(int, input().split())
if x < y:
    x, y = y, x
if d < y:
    print(d + 1)
elif d < x:
    print(y + 1)
elif d <= x + y:
    print(x + y - d + 1)
else:
    print(0)
