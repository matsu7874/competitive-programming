N = int(input())
a,b = [int(x)-1 for x in input().split()]
M = int(input())
P = []
path = [[999 for j in range(N)] for i in range(N)]
for i in range(N):
    path[i][i] = 0
for _ in range(M):
    x,y = [int(x)-1 for x in input().split()]
    P.append((x,y))
    path[x][y] = 1
    path[y][x] = 1

in_list = [[] for i in range(N)]
for i in range(N):
    for j in range(N):
        if (j,i) in P or (i,j) in P:
            in_list[i].append(j)

for k in range(N):
    for i in range(N):
        for j in range(N):
            path[i][j] = min(path[i][j], path[i][k]+path[k][j])
path_len = path[a][b]

path_num = [0 for i in range(N)]
for i in range(N):
    if b in in_list[i]:
        path_num[i] = 1
    else:
        path_num[i] = 0
lock = [0 for i in range(N)]
lock[b]=-1
for i in range(path_len):
    for j in range(N):
        for e in in_list[j]:
            if lock[e] != -1:
                lock[e] += path_num[j]
    for j in range(N):
        if lock[j]>0:
            path_num[j] += lock[j]
            lock[j] = -1
print(path_num[a] % 1000000007)
