import copy
H, W = map(int, input().split())
S = []
for i in range(H):
    S.append([c for c in input()])

cnt_black = sum(S[i].count('#') for i in range(H))
if cnt_black % 2 == 1 or cnt_black == 0:
    print('NO')
    exit()

for h in range(H):
    for w in range(-W + 1, W):
        if h == 0 and w <= 0:
            continue
        s = [row[:] for row in S]
        cnt = 0
        flg = False
        for i in range(H):
            for j in range(W):
                if s[i][j] == '#':
                    if 0 <= i + h < H and 0 <= j + w < W and s[i + h][j + w] == '#':
                        s[i][j] = 'r'
                        s[i + h][j + w] = 'b'
                        cnt += 2
                    else:
                        flg = True
                        break
            if flg:
                break
        if cnt == cnt_black:
            print('YES')
            exit()
print('NO')
