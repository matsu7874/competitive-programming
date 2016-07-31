n,m=map(int, input().split())
red = [False for i in range(n)]
red[0] = True
cnt = [1 for i in range(n)]
for i in range(m):
    x,y=map(int, input().split())
    x -= 1
    y -= 1
    red[y] |= red[x]
    cnt[y] += 1
    cnt[x] -= 1
    if cnt[x] == 0:
        red[x] = False
print(red.count(True))