H, W = map(int, input().split())
C = [[int(x) for x in input().split()] for i in range(H)]
for i in range(H):
    for j in range(W):
        if (i + j) % 2:
            C[i][j] *= -1
cs = [[0] * W for i in range(H)]
cs[0][0] = C[0][0]
for i in range(1, H):
    cs[i][0] = cs[i - 1][0] + C[i][0]
for i in range(1, W):
    cs[0][i] = cs[0][i - 1] + C[0][i]
for i in range(1, H):
    for j in range(1, W):
        cs[i][j] = cs[i - 1][j] + cs[i][j - 1] - cs[i - 1][j - 1] + C[i][j]

max_cell = 0
for i in range(H):
    for j in range(W):
        for y in range(i+1):
            for x in range(j+1):
                if i==y and j==x:
                    continue
                s = cs[i][j]
                if i-y > 0:
                    s -= cs[i - y - 1][j]
                if j-x > 0:
                    s -= cs[i][j - x - 1]
                if i-y > 0 and j-x > 0:
                    s += cs[i - y - 1][j - x - 1]
                if s == 0:
                    max_cell = max(max_cell, (i - y + 1) * (j - x + 1))
                    # print(i, j, y, x, (i - y + 1) * (j - x + 1))
print(max_cell)
