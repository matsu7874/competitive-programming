N, X = map(int, input().split())
tree = [[] for i in range(N)]
for i in range(N - 1):
    x, y, c = map(int, input().split())
    tree[x - 1].append((y - 1, c))
    tree[y - 1].append((x - 1, c))

cost = [-1] * N
cost[0] = 0

queue = [0]
while queue:
    v = queue.pop()
    for n, c in tree[v]:
        if cost[n] >= 0:
            continue
        queue.append(n)
        cost[n] = cost[v] ^ c

frequency = {}
for i in range(N):
    if cost[i] in frequency:
        frequency[cost[i]]+=1
    else:
        frequency.update({cost[i]:1})
cnt = 0
if X==0:
    for k,v in frequency.items():
        cnt += v*(v-1)//2
else:
    for k,v in frequency.items():
        x = k^X
        if x in frequency and k<x:
            cnt += v*frequency[x]
print(cnt)
