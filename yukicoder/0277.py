import collections

N = int(input())
tree = [[] for i in range(N)]
for i in range(N - 1):
    x, y = map(int, input().split())
    tree[x - 1].append(y - 1)
    tree[y - 1].append(x - 1)

L = [N * 2] * N
dq = collections.deque()

L[0] = 0
dq.append(0)

for i in range(N):
    if len(tree[i]) == 1:
        L[i] = 0
        dq.append(i)

while dq:
    cur = dq.popleft()
    for t in tree[cur]:
        if L[t] <= L[cur] + 1:
            continue
        L[t] = L[cur] + 1
        dq.append(t)

for i in range(N):
    print(L[i])
