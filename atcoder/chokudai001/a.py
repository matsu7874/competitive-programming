A = [list(map(int, input().split())) for i in range(30)]
turn = sum([sum(A[i]) for i in range(30)])
x = 1
y = 1
while turn:
    if A[y][x] == 0:
        x += 1
        if x == 30:
            y += 1
            x = 0
            if y == 30:
                y = 0
        continue

    A[y][x] -= 1
    print(y+1, x+1)
    turn -= 1

    if A[y][x] > 0:
        if y > 0 and A[y - 1][x] == A[y][x]:
            y -= 1
        elif y < (30 - 1) and A[y + 1][x] == A[y][x]:
            y += 1
        elif x > 0 and A[y][x - 1] == A[y][x]:
            x -= 1
        elif x < (30 - 1) and A[y][x + 1] == A[y][x]:
            x += 1
