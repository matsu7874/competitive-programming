(N, M) = map(int, input().split())
adj = [[99 for _ in range(N)] for _ in range(N)]
for i in range(N):
    adj[i][i] = 0

for i in range(M):
    (a, b) = map(int, input().split())
    adj[a - 1][b - 1] = 1
    adj[b - 1][a - 1] = 1

for i in range(N):
    for j in range(N):
        for k in range(N):
            if adj[i][k] + adj[k][j] < adj[i][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

for i in range(N):
    print(adj[i].count(2))
