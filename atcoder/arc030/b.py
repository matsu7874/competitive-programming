n, x = map(int, input().split())
x -= 1
H = list(map(int, input().split()))
edges = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

node = n
while True:
    change = False
    for i in range(n):
        if H[i] == 1 or i == x:
            continue
        if len(edges[i]) == 1:
            v = edges[i][0]
            edges[v].remove(i)
            edges[i] = []
            node -= 1
            change = True
    if not change:
        break
print(node * 2 - 2)
