N, M = map(int, input().split())
R = [0] * (N + 1)
C = []
for i in range(M):
    s, t = map(int, input().split())
    C.append((s - 1, t - 1))
    R[s - 1] += 1
    R[t] -= 1
for i in range(1, N):
    R[i] += R[i - 1]
L = [0] * N
cnt = 0
for i in range(N):
    if R[i] > 1:
        cnt += 1
        L[i] = cnt
    else:
        cnt = 0
sabotagable = []
for i in range(M):
    if L[C[i][1]] >= C[i][1] - C[i][0] + 1:
        sabotagable.append(i + 1)
print(len(sabotagable))
for v in sabotagable:
    print(v)
