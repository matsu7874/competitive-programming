cells = [input() for i in range(8)]
min_w = 9
min_b = 9
for i in range(8):
    w = 0
    b = 0
    for j in range(7, -1, -1):
        if cells[j][i] == 'W':
            w += 1
        elif cells[j][i] == 'B' and w == 0:
            min_b = min(min_b, 7 - j)
    for j in range(8):
        if cells[j][i] == 'B':
            b += 1
        if cells[j][i] == 'W' and b == 0:
            min_w = min(min_w, j)
if min_b < min_w:
    print('B')
else:
    print('A')
