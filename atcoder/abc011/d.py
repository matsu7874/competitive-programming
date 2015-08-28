import copy
N, D = map(int, input().split())
X, Y = map(int, input().split())
if X % D != 0 or Y % D != 0:
    print(0.0)
    exit()
X //= D
Y //= D
T = [[0 for j in range(2 * N + 1)] for i in range(2 * N + 1)]
Direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T[N][N] = 1
for i in range(N):
    Tn = [T[i][:] for i in range(N)]
    for j in range(N):
        for k in range(N):
            if Tn[j][k] > 0:
                for l in range(4):
                    + Direction[l]
    Tn[0][0] += 1
    T = [Tn[i][:] for i in range(N)]
    print(Tn[0])
