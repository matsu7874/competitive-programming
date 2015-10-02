N, K = map(int, input().split())
A = [int(input()) for i in range(N)]
if K == 1:
    print(N)
    exit()
cnt = 0
length = 1
for i in range(1,N):
    if A[i-1] < A[i]:
        length += 1
    else:
        length = 1
    if length >= K:
        cnt += 1
print(cnt)
