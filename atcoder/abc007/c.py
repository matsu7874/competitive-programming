import queue
R, C = [int(x) for x in input().split()]
sy, sx = [int(x) - 1 for x in input().split()]
gy, gx = [int(x) - 1 for x in input().split()]
T = [input() for i in range(R)]
distance = [[9999999999 for j in range(C)] for i in range(R)]
distance[sy][sx] = 0
q = queue.Queue()
q.put((sy, sx))
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while not q.empty():
    c = q.get()
    for d in D:
        if 0 <= c[0] + d[0] < R and 0 <= c[1] + d[1] < C and T[c[0] + d[0]][c[1] + d[1]] == '.':
            if c[0] + d[0] == gy and c[1] + d[1] == gx:
                print(distance[c[0]][c[1]] + 1)
                exit()
            if distance[c[0] + d[0]][c[1] + d[1]] > distance[c[0]][c[1]] + 1:
                distance[c[0] + d[0]][c[1] + d[1]] = distance[c[0]][c[1]] + 1
                q.put((c[0] + d[0], c[1] + d[1]))
