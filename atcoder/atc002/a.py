import heapq
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [input() for i in range(r)]

visited = [False for i in range(r*c)]
hq = [(0, sy-1, sx-1)]
while hq:
    cost, y, x = heapq.heappop(hq)
    if y == gy-1 and x == gx-1:
        print(cost)
        exit()

    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        ny = y + dy
        nx = x + dx
        if maze[ny][nx] == '.' and not visited[ny*c+nx]:
            heapq.heappush(hq,(cost+1, ny, nx))
            visited[ny*c+nx] = True
