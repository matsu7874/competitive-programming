N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
P = [0] * 101
for i in range(N):
    P[B[i]] += A[i]
if max(P) == P[0]:
    print('YES')
else:
    print('NO')
