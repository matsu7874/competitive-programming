# TODO: solve
func = [1, 1, 2, 6, 24, 120, 720]


def calc(a, b, c, d):
    total = 0
    if a == b and b == c and c == d:
        return 24 * a * (100 - a) + 601
    elif a > b and b == c and c == d:
        p = [1, 3]
    elif a == b and b > c and c == d:
        p = [2, 2]
    elif a > b and b > c and c == d:
        p = [1, 1, 2]
    elif a == b and b == c and c > d:
        p = [3, 1]
    elif a > b and b == c and c > d:
        p = [1, 2, 1]
    elif a == b and b > c and c > d:
        p = [2, 1, 1]
    elif a > b and b > c and c > d:
        p = [1, 1, 1, 1]
    else:
        print(a, b, c, d)
        exit()
    t = func[p[0]+1] * func[p[-1]+1]
    if len(p) > 2:
        t *= func[p[1]]
    return 720//t*((100-a)*(p[0]+1)+1)*(d*(p[-1]+1)+1)


x = float(input())
y = int(x * 4)
total = 0
for a in range(int(x), min(100, y) + 1):
    for b in range(0, min(int(2 * x), a) + 1):
        if b>a:
            continue
        for c in range(0, min(int(4 / 3 * x), b) + 1):
            if c>b:
                continue
            d = y - a - b - c
            if 0 <= d <= c:
                total += calc(a, b, c, d)
print(total)
