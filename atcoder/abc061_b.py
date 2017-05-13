n,m = map(int, input().split())
g = [0 for i in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    g[a] += 1
    g[b] += 1
for i in range(n):
    print(g[i])
