while True:
    rx = 10
    ry = 10
    n = int(input())
    if n == 0:
        exit()
    gems = [[0 for j in range(21)] for i in range(21)]
    for _ in range(n):
        (x, y) = [int(x) for x in input().split()]
        gems[x][y] = 1
    m = int(input())
    for _ in range(m):
        (d, l) = input().split()
        if d=='N':
            for i in range(1, int(l)+1):
                gems[rx][ry+i] = 0
            ry = ry+int(l)
        elif d=='W':
            for i in range(1, int(l)+1):
                gems[rx-i][ry] = 0
            rx = rx-int(l)
        elif d=='E':
            for i in range(1, int(l)+1):
                gems[rx+i][ry] = 0
            rx = rx+int(l)
        elif d=='S':
            for i in range(1, int(l)+1):
                gems[rx][ry-i] = 0
            ry = ry-int(l)
    if sum([sum(gems[i]) for i in range(21)])==0:
        print('Yes')
    else:
        print('No')
