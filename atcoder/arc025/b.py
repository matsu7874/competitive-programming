H, W = map(int, input().split())
C = [[int(x) for x in input().split()] for i in range(H)]
for i in range(H):
    for j in range(W):
        if (i + j) % 2:
            C[i][j] *= -1

cs = [[0] * (W + 1) for i in range(H + 1)]
for i in range(H):
    for j in range(W):
        cs[i + 1][j + 1] = cs[i][j + 1] + cs[i + 1][j] - cs[i][j] + C[i][j]

max_cell = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        for y in range(i+1):
            for x in range(j+1):
                if i==y and j == y:
                    continue
                if cs[i][j] - cs[y][j] - cs[i][x] + cs[y][x] == 0:
                    max_cell = max(max_cell, (i - y) * (j - x))
print(max_cell)
