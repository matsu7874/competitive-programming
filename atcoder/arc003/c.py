import queue
N, M = map(int, input().split())

T = [input() for i in range(N)]
TI = [[10 for j in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        if T[i][j] in 'sg':
            TI[i][j] = T[i][j]
        elif T[i][j] == '#':
            TI[i][j] = 0
        else:
            TI[i][j] = int(T[i][j])

Q = queue.PriorityQueue()
for i in range(N):
    for j in range(M):
        if T[i][j] == 's':
            Q.put((-10, 0, i, j))
            break

D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
path = [[0.000001 for j in range(M)] for i in range(N)]
while not Q.empty():
    q = Q.get()
    if path[q[2]][q[3]] <= q[0]:
        continue
    else:
        path[q[2]][q[3]] = q[0]

    for d in D:
        if 0 <= q[2] + d[0] < N and 0 <= q[3] + d[1] < M and T[q[2] + d[0]][q[3] + d[1]] not in '#s':
            if T[q[2] + d[0]][q[3] + d[1]] == 'g':
                print(-q[0])
                exit()
            else:
                Q.put((max(-TI[q[2] + d[0]][q[3] + d[1]] * 0.99 ** (q[1] + 1), q[0]),
                       q[1] + 1,  q[2] + d[0], q[3] + d[1]))

print(-1)
