N, M = map(int, input().split())
L = []
R = []
for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
w = [0 for i in range(M)]
for i in range(N):
    for j in range(L[i], R[i] + 1):
        w[j] += 1
if all(w[i] + w[M - i - 1] <= 2 for i in range(N)):
    print('YES')
else:
    print('NO')
