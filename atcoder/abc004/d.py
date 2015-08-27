(r, g, b) = [int(x) for x in input().split()]

rl = (r - 1) // 2 * (-1) - (r - 1) % 2 - 100
rr = (r - 1) // 2 - 100
gl = (g - 1) // 2 * (-1) - (g - 1) % 2
gr = (g - 1) // 2
bl = (b - 1) // 2 * (-1) + 100
br = (b - 1) // 2 + (b - 1) % 2 + 100


def calc(c, l, r):
    if c < l:
        return (r - l + 1) * (l - c) + (r - l + 1) * (r - l) // 2
    elif r < c:
        return (r - l + 1) * (c - r) + (r - l + 1) * (r - l) // 2
    else:
        return (c - l) * (c - l + 1) // 2 + (r - c) * (r - c + 1) // 2


def calc_all(rl, rr, gl, gr, bl, br):
    return calc(-100, rl, rr) + calc(0, gl, gr) + calc(100, bl, br)
if rr >= gl:
    d = rr - gl + 1
    rr -= d
    rl -= d
if gr >= bl:
    d = gr - bl + 1
    bl += d
    br += d
moved = True
while moved:
    moved = False
    if gr + 1 == bl:
        if calc_all(rl, rr, gl, gr, bl, br) > calc_all(rl + 1, rr + 1, gl + 1, gr + 1, bl + 1, br + 1):
            rl += 1
            rr += 1
            gl += 1
            gr += 1
            bl += 1
            br += 1
            moved = True
    else:
        if calc(-100, rl, rr) + calc(0, gl, gr) > calc(-100, rl + 1, rr + 1) + calc(0, gl + 1, gr + 1):
            rl += 1
            rr += 1
            gl += 1
            gr += 1
            moved = True
moved = True
while moved:
    moved = False
    if rr + 1 == gl:
        if calc_all(rl, rr, gl, gr, bl, br) > calc_all(rl - 1, rr - 1, gl - 1, gr - 1, bl - 1, br - 1):
            rl -= 1
            rr -= 1
            gl -= 1
            gr -= 1
            bl -= 1
            br -= 1
            moved = True
    else:
        if calc(100, bl, br) + calc(0, gl, gr) > calc(100, bl - 1, br - 1) + calc(0, gl - 1, gr - 1):
            bl -= 1
            br -= 1
            gl -= 1
            gr -= 1
            moved = True
# print(rl,rr,gl,gr,bl,br)
print(calc_all(rl, rr, gl, gr, bl, br))
