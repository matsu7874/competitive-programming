import queue
N, M = map(int, input().split())
T = [input() for i in range(N)]
TI = [[0 for j in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        if T[i][j] in 'sg#':
            TI[i][j] = T[i][j]
        else:
            TI[i][j] = int(T[i][j])
Q = queue.PriorityQueue()
for i in range(N):
    for j in range(M):
        if T[i][j] == 's':
            Q.put((-10, 0, i, j))
            break
lower_limit = 1
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
path_exist = False
path = [[0 for j in range(M)] for i in range(N)]
while not Q.empty():
    q = Q.get()
    if path[q[2]][q[3]] <= q[0]:
        continue
    else:
        path[q[2]][q[3]] = q[0]

    if q[0] > lower_limit:
        continue
    else:
        for d in D:
            if 0 <= q[2] + d[0] < N and 0 <= q[3] + d[1] < M and T[q[2] + d[0]][q[3] + d[1]] not in '#s':
                if T[q[2] + d[0]][q[3] + d[1]] == 'g':
                    path_exist = True
                    lower_limit = min(lower_limit, q[0])
                    print(-lower_limit)
                    exit()
                else:
                    Q.put((max(-TI[q[2] + d[0]][q[3] + d[1]] * 0.99 ** (q[1] + 1), q[0]),
                           q[1] + 1,  q[2] + d[0], q[3] + d[1]))
if path_exist:
    print(-lower_limit)
else:
    print(-1)
