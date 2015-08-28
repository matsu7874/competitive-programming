import queue
X, Y = map(int, input().split())
Q = queue.Queue()
Q.put((0, 0, 0))
D = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
while not Q.empty():
    q = Q.get()
    if q[0] > 3:
        continue
    elif q[1] == X and q[2] == Y:
        print('YES')
        exit()
    else:
        for d in D:
            Q.put((q[0] + 1, q[1] + d[0], q[2] + d[1]))
print('NO')
