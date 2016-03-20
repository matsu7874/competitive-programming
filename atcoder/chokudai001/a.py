A = [list(map(int, input().split())) for i in range(30)]

x = 0
y = 0
s = 1
while any([any([A[i][j] > 0 for j in range(30)]) for i in range(30)]):
    if s == 1:
        if A[y][x] == 0:
            x += 1
            if x == 30:
                y += 1
                x = 0
                if y == 30:
                    y = 0
        else:
            s = 2
    if s == 2:
        A[y][x] -= 1
        print(y, x)
        if A[y][x] == 0:
            s = 1
            continue
        if y > 0 and A[y - 1][x] == A[y][x]:
            y -= 1
        elif y < (30 - 1) and A[y + 1][x] == A[y][x]:
            y += 1
        elif x > 0 and A[y][x - 1] == A[y][x]:
            x -= 1
        elif x < (30 - 1) and A[y][x + 1] == A[y][x]:
            x += 1
        else:
            s = 1
