n, m = map(int, input().split())
a = 0
b = 0
c = 0
if m % 2 == 1:
    b = 1
    m -= 3
    n -= 1
m //= 2
c = m - n
a = n - c
if a < 0 or c < 0:
    a = -1
    b = -1
    c = -1
print(a, b, c)
