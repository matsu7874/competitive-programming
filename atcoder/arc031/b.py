import collections
A = [input() for i in range(10)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(10):
    for j in range(10):
        is_connected = [[A[i][j] == 'x' for j in range(10)] for i in range(10)]
        is_connected[i][j] = True
        dq = collections.deque()
        dq.append((i, j))
        while dq:
            y, x = dq.popleft()
            for d in directions:
                if 0 <= y + d[0] < 10 and 0 <= x + d[1] < 10 and A[y + d[0]][x + d[1]] == 'o':
                    if not is_connected[y + d[0]][x + d[1]]:
                        is_connected[y + d[0]][x + d[1]] = True
                        dq.append((y + d[0], x + d[1]))
        if all(all(is_connected[i]) for i in range(10)):
            print('YES')
            exit()
print('NO')
