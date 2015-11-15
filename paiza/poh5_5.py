import random
T = []
for i in range(4):
    T.append([x for x in input().split()])
cnt = 0
y = ['*' in t for t in T].index(True)
x = T[y].index('*')
while cnt<15:
    while T[cnt//4][cnt%4] == str(cnt+1):
        cnt += 1
    flg = True
    for (rx,ry) in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0<=x+rx<=3 and 0<=y+ry<=3 and int(T[y+ry][x+rx])==cnt+1:
            T[y][x],T[y+ry][x+rx] = T[y+ry][x+rx],T[y][x]
            print(T[y][x])
            y = y+ry
            x = x+rx
            cnt += 1
            flg = False
    if flg:
        (rx,ry) = random.choice([(-1,0),(1,0),(0,-1),(0,1)])
        if 0<=x+rx<=3 and 0<=y+ry<=3 and int(T[y+ry][x+rx])>cnt:
            T[y][x],T[y+ry][x+rx] = T[y+ry][x+rx],T[y][x]
            print(T[y][x])
            y = y+ry
            x = x+rx
