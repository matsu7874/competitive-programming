A = [list(map(int, input().split())) for i in range(30)]
turn = sum([sum(A[i]) for i in range(30)])


def search_max_position(A):
    max_x = 0
    max_y = 0
    max_v = A[0][0]
    for i in range(30):
        for j in range(30):
            if A[i][j] > max_v:
                max_v = A[i][j]
                max_y = i
                max_x = j
    return max_x, max_y


def score(y, x, A, dep):
    if dep == 0:
        s = [0]
        if y > 0 and A[y - 1][x] <= A[y][x]:
            ss = 1
            if A[y - 1][x] == A[y][x]:
                ss += 1000
            s.append(score(y - 1, x, A, dep + 1) + ss)
        elif y < (30 - 1) and A[y + 1][x] <= A[y][x]:
            ss = 1
            if A[y + 1][x] == A[y][x]:
                ss += 1000
            s.append(score(y + 1, x, A, dep + 1) + ss)
        elif x > 0 and A[y][x - 1] <= A[y][x]:
            ss = 1
            if A[y][x - 1] == A[y][x]:
                ss += 1000
            s.append(score(y, x - 1, A, dep + 1) + ss)
        elif x < (30 - 1) and A[y][x + 1] <= A[y][x]:
            ss = 1
            if A[y][x + 1] == A[y][x]:
                ss += 1000
            s.append(score(y, x + 1, A, dep + 1) + ss)
        return max(s)
    else:
        s = [0]
        if y > 0 and A[y - 1][x] < A[y][x]:
            ss = dep
            if A[y - 1][x] == A[y][x] - 1:
                ss += 1000
            s.append(score(y - 1, x, A, dep + 1) + ss)
        elif y < (30 - 1) and A[y + 1][x] < A[y][x]:
            ss = dep
            if A[y + 1][x] == A[y][x] - 1:
                ss += 1000
            s.append(score(y - 1, x, A, dep + 1) + ss)
        elif x > 0 and A[y][x - 1] < A[y][x]:
            ss = dep
            if A[y][x - 1] == A[y][x] - 1:
                ss += 1000
            s.append(score(y - 1, x, A, dep + 1) + ss)
        elif x < (30 - 1) and A[y][x + 1] < A[y][x]:
            ss = dep
            if A[y][x + 1] == A[y][x] - 1:
                ss += 1000
            s.append(score(y - 1, x, A, dep + 1) + ss)
        return max(s)

x, y = search_max_position(A)

while turn:
    A[y][x] -= 1
    print(y + 1, x + 1)
    turn -= 1

    if A[y][x] > 0:
        q = []
        if y > 0 and A[y - 1][x] == A[y][x]:
            q.append((y - 1, x))
        elif y < (30 - 1) and A[y + 1][x] == A[y][x]:
            q.append((y + 1, x))
        elif x > 0 and A[y][x - 1] == A[y][x]:
            q.append((y, x - 1))
        elif x < (30 - 1) and A[y][x + 1] == A[y][x]:
            q.append((y, x + 1))

        if len(q) == 0:
            x, y = search_max_position(A)
        elif len(q) == 1:
            x, y = q[0][1], q[0][0]
        elif len(q) >= 2:
            p = []
            for qy, qx in q:
                p.append((score(qy, qx, A, 0), qy, qx))
            p.sort()
            p.reverse()
            x, y = p[0][2], p[0][1]
    else:
        x, y = search_max_position(A)
