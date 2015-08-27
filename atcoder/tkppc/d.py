def str_to_int(c):
    if c == 'H':
        return 0
    else:
        return int(c)

N,R,C = [int(x) for x in input().split()]
S = []
for i in range(N*R):
    S.append(input())
cost = [[[str_to_int(S[i*R+j][k]) for k in range(C)] for j in range(R)] for i in range(N)]
adj = [[[[] for k in range(C)] for j in range(R)] for i in range(N)]
for n in range(N):
    for r in range(R):
        for c in range(C-1):
            adj[n][r][c].append([n, r, c+1])
            adj[n][r][c+1].append([n, r, c])
for n in range(N):
    for r in range(R-1):
        for c in range(C):
            adj[n][r][c].append([n, r+1, c])
            adj[n][r+1][c].append([n, r, c])
for n in range(N-1):
    for r in range(R):
        for c in range(C):
            if S[n*R+r][c] == 'H':
                adj[n+1][r][c].append([n, r, c])

adj = [[[[] for k in range(C)] for j in range(R)] for i in range(N)]
visited = [[False for k in range(C)] for j in range(R)] for i in range(N)]
prev[0][0] = (0,0)

min_cost = 1000000000
for n in range(N):
    for r in range(R):
        for c in range(C):
            visited[n][r][c] = True



print(cost[N*R-1][C-1])
