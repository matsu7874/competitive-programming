x, y, W = input().split()
x = int(x)
y = int(y)
C = [input() for i in range(9)]
ans = [0, 0, 0, 0]
direction = ['R', 'L', 'U', 'D', 'RU', 'RD', 'LU', 'LD']
d = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
dx = d[direction.index(W)][0]
dy = d[direction.index(W)][1]

for i in range(4):
    ans[i] = C[y - 1][x - 1]
    x += dx
    if x < 1:
        x = 2
        dx = -dx
    if 9 < x:
        x = 8
        dx = -dx
    y += dy
    if y < 1:
        y = 2
        dy = -dy
    if 9 < y:
        y = 8
        dy = -dy
print(''.join(ans))
