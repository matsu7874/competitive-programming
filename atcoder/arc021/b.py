N = int(input())
B = [int(input()) for i in range(N)]
A = [0] * N
for i in range(1, N):
    A[i] = A[i - 1] ^ B[i - 1]
if A[N - 1] != B[N - 1]:
    print(-1)
else:
    for a in A:
        print(a)
