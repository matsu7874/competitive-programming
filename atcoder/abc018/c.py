h, w, k = map(int, input().split())
s = [input() for i in range(h)]
if k * 2 - 1 > min(h, w):
    print(0)
    exit()

def check(y, x, k):
    for i in range(-k + 1, k):
        if cx[y + i][x + k - 1 - abs(i)] < (k - 1 - abs(i)) * 2 + 1:
            return False
    return True

cx = [[0 for j in range(w)] for i in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            if j == 0:
                cx[i][j] = 1
            else:
                cx[i][j] = cx[i][j - 1] + 1
        else:
            cx[i][j] = 0
total = 0
# 中心の座標
for i in range(k - 1, h - k + 1):
    for j in range(k - 1, w - k + 1):
        if check(i, j, k):
            total += 1
print(total)
