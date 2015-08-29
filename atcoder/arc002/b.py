def is_leap_year(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False

y, m, d = map(int, input().split('/'))
while y % (m * d) != 0:
    if d == 31:
        d = 1
        m += 1
    elif d == 30 and m in [4, 6, 9, 11]:
        d = 1
        m += 1
    elif d == 29 and m == 2:
        d = 1
        m += 1
    elif d == 28 and m == 2 and not is_leap_year(y):
        d = 1
        m += 1
    else:
        d += 1
    if m == 13:
        m = 1
        y += 1
print('{0:02d}/{1:02d}/{2:02d}'.format(y, m, d))
