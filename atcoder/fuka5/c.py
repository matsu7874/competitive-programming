while True:
    w,h,p=map(int, input().split())
    if w ==0 and h==0 and p==0:
        exit()
    z = [list(map(int, input().split())) for i in range(h)]
    visited = [[False for j in range(w)] for i in range(h)]
    queue = []
    cnt = 0
    for i in range(p):
        x,y=map(int, input().split())
        queue.append((x,y))

    while queue:
        x,y = queue.pop()
        if visited[y][x]:
            continue
        visited[y][x] = True
        cnt += 1
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx = x+dx
            ny = y+dy
            if 0<=nx<w and 0<=ny<h and z[ny][nx] < z[y][x]:
                queue.append((nx,ny))
    print(cnt)
    
        