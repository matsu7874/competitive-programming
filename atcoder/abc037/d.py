import sys
sys.setrecursionlimit(1000*1000)
h, w = map(int, input().split())
maze = [list(map(int, input().split())) for i in range(h)]
route = [[0 for j in range(w)] for i in range(h)]
total = 0


def search(Y, X):


    if route[Y][X] > 0:
        return route[Y][X]
    y = Y
    x = X
    local = 1
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < h and 0 <= nx < w and maze[y][x] < maze[ny][nx]:
            local += search(ny, nx)
    route[Y][X] = local
    return local


for i in range(h):
    for j in range(w):
        total = (total + search(i, j)) % (10**9 + 7)
print(total % (10**9 + 7))
