N, M = map(int, input().split())
S = [input() for i in range(N)]
path = [[1000000000 for j in range(M)] for i in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
h = []
for i in range(N):
    for j in range(M):
        if S[i][j] == 'C':
            path[i][j] = 0
            h.append((0, i, j))
            break

path_start = 0
path_goal = 0
while h != []:
    q = h.pop(0)
    for i in range(4):
        if path[q[1] + dy[i]][q[2] + dx[i]] <= q[0] + 1:
            continue
        else:
            path[q[1] + dy[i]][q[2] + dx[i]] = q[0]
        if S[q[1] + dy[i]][q[2] + dx[i]] == '#':
            continue
        if S[q[1] + dy[i]][q[2] + dx[i]] == 'S':
            path_start = q[0] + 1
            if path_goal > 0:
                print(path_start + path_goal)
                exit()
        elif S[q[1] + dy[i]][q[2] + dx[i]] == 'G':
            path_goal = q[0] + 1
            if path_start > 0:
                print(path_start + path_goal)
                exit()
        h.append((q[0] + 1, q[1] + dy[i], q[2] + dx[i]))
print(-1)
