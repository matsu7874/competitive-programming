def is_cross(x1, x2, x3, x4, y1, y2, y3, y4):
    if ((x1 - x2) * (y3 - y1) + (y1 - y2) * (x1 - x3)) * ((x1 - x2) * (y4 - y1) + (y1 - y2) * (x1 - x4)) < 0:
        if ((x3 - x4) * (y1 - y3) + (y3 - y4) * (x3 - x1)) * ((x3 - x4) * (y2 - y3) + (y3 - y4) * (x3 - x2)) < 0:
            return True
    return False

(Ax, Ay, Bx, By) = map(int, input().split())
N = int(input())
X = []
Y = []
for i in range(N):
    (x, y) = map(int, input().split())
    X.append(x)
    Y.append(y)
cnt = 0
for i in range(1, N):
    if is_cross(Ax, Bx, X[i - 1], X[i], Ay, By, Y[i - 1], Y[i]):
        cnt += 1
if is_cross(Ax, Bx, X[0], X[N - 1], Ay, By, Y[0], Y[N - 1]):
    cnt += 1
print((cnt // 2) + 1)
