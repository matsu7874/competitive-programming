cx, cy, r = map(int, input().split())
a, b, c, d = map(int, input().split())
if a > c:
    a, c = c, a
if b > d:
    b, d = d, b
ps = [(a, b), (a, d), (c, b), (c, d)]
if all([(cx - x)**2 + (cy - y)**2 <= r * r for x, y in ps]):
    print('YES')
    print('NO')
    exit()

if cx - r < a or c < cx + r or cy - r < b or d < cy + r:
    print('YES')
else:
    print('NO')

print('YES')
