N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
A.reverse()
B.sort()
B.reverse()
cur_a = 0
cur_b = 0
while cur_a < N and cur_b < M:
    if B[cur_b] <= A[cur_a]:
        cur_b += 1
        cur_a += 1
    else:
        cur_a += 1
if cur_b == M:
    print('YES')
else:
    print('NO')
