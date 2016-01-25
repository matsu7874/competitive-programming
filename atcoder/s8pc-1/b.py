def is_cuttable(x,y):
    cnt_t = 0
    cnt_b = 0
    for p, q in S:
        if y * p == x * q:
            return False
        elif y * p > x * q:
            cnt_b += 1
        else:
            cnt_t += 1
    return cnt_b == cnt_t

def main():
    cuttable = []
    for i in range(1,H):
        if is_cuttable(W,i):
            cuttable.append((W,i))
    for i in range(1,W):
        if is_cuttable(i,H):
            cuttable.append((i,H))
    if is_cuttable(W,H):
        cuttable.append((W,H))
    cuttable.sort()
    if not cuttable:
        print(-1)
    for p in cuttable:
        print('('+str(p[0])+','+str(p[1])+')')

H, W, N = map(int, input().split())
S = []
for i in range(N):
    x, y = map(int, input().split())
    S.append((x, y))
main()
