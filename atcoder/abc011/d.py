import copy
N, D = map(int, input().split())
X, Y = map(int, input().split())
if X % D != 0 or Y % D != 0:
    print(0.0)
    exit()
X //= D
Y //= D
T = [[0 for j in range(2 * N + 1)] for i in range(2 * N + 1)]
