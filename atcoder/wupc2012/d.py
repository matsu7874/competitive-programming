N = int(input())
A = []
for i in range(N):
    a = map(int, input().split())
    A.append(list(a))
for i in range(N - 1, 0, -1):
    for j in range(i):
        A[i - 1][j] += max(A[i][j], A[i][j + 1])
print(A[0][0])
