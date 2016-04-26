import heapq
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [input() for i in range(r)]

visited = [False for i in range(r*c)]
hq = [(abs(gy-sy)**2 + abs(gx-sx), 0, sy-1, sx-1)]
while hq:
    heuristic, cost, y, x = heapq.heappop(hq)
    if y == gy-1 and x == gx-1:
        print(cost)
        exit()

    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        ny = y + dy
        nx = x + dx
        heuristic = abs(gy - ny) + abs(gx - nx) + cost
        if maze[ny][nx] == '.' and not visited[ny*c+nx]:
            heapq.heappush(hq,(heuristic,cost+1, ny, nx))
            visited[ny*c+nx] = True
