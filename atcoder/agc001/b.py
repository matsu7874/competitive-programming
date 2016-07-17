n, x = map(int, input().split())
total = n
h = n - x
w = x
while h and w:
    if h == w:
        total += h
        h = 0
        w = 0
        break
    elif h > w:
        total += (h // w) * 2 * w
        h %= w
    else:
        total += (w // h) * 2 * h
        w %= h
total -= max(w, h)
print(total)
