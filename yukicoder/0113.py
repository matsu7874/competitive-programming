S = input()
e = 0
n = 0
for c in S:
    if c == 'N':
        n += 1
    elif c == 'E':
        e += 1
    elif c == 'W':
        e -= 1
    elif c == 'S':
        n -= 1
print((abs(n)**2 + abs(e)**2)**0.5)
