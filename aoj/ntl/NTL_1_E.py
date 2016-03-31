a, b = map(int, input().split())

r0 = a
r1 = b
x0 = 1
x1 = 0
y0 = 0
y1 = 1
while r1 > 0:
    q1 = r0 // r1
    r2 = r0 % r1
    x2 = x0 - q1 * x1
    y2 = y0 - q1 * y1
    r0 = r1
    r1 = r2
    x0 = x1
    x1 = x2
    y0 = y1
    y1 = y2
print(x0,y0)
