ht, mt = map(int, input().split())
h, m = map(int, input().split())
while h * 60 + m < 12 * 60:
    if ((h + 6) % 12) * 60 + ((m + 30) % 60) <= ht * 60 + mt:
        print('Yes')
        exit()
    m += 1
    if m >= 59:
        m = 0
        h += 1
print('No')
