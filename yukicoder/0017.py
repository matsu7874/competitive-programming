INF = 9999999999
N = int(input())
S = [int(input()) for i in range(N)]
M = int(input())
path = [[INF for j in range(N)] for i in range(N)]
for i in range(N):
    path[i][i] = 0
for i in range(M):
    a, b, c = map(int, input().split())
    path[a][b] = c
    path[b][a] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            if path[i][j] > path[i][k] + path[k][j]:
                path[i][j] = path[i][k] + path[k][j]
min_path = INF
for i in range(1, N - 1):
    for j in range(1, N - 1):
        if i == j:
            continue
        path_cost = path[0][i] + path[i][j] + path[j][N - 1]
        if min_path > path_cost + S[i] + S[j]:
            min_path = min(min_path, path_cost + S[i] + S[j])
print(min_path)
