import collections

W, H = map(int, input().split())
maze = [input() for i in range(H)]
visited = [False] * (W * H)
space = []

i = 0
while maze[i//W][i%W] == '#':
    i += 1
dq = collections.deque()
dq.append(i)

while dq:
    q = dq.popleft()
    if visited[q]:
        continue
    visited[q] = True
    space.append(q)
    for d in (-W, -1, 1, W):
        if q + d < 0 or W * H <= q + d:
            continue
        if d in (-1, 1) and (q + d) // W != q // W:
            continue
        if maze[(q+d)//W][(q+d)%W] == '.':
            dq.append(q+d)

while maze[i//W][i%W] == '#' or visited[i]:
    i += 1

visited = [W*H] * (W * H)
dq = collections.deque()
dq.append((i,0))
min_cost = W*H
while dq:
    q,v = dq.popleft()
    if q in space:
        min_cost = min(min_cost,v)
        # print(i,q,v)
        continue
    if visited[q] <= v:
        continue
    else:
        visited[q] = v
    for d in (-W, -1, 1, W):
        if q + d < 0 or W * H <= q + d:
            continue
        if d in (-1, 1) and (q + d) // W != q // W:
            continue
        if maze[(q+d)//W][(q+d)%W] == '#':
            dq.append((q+d,v+1))
        else:
            dq.append((q+d,v))
print(min_cost)
