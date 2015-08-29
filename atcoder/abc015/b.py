import math
N = int(input())
A = list(map(int, input().split()))
cnt = 0
total = 0
for i in range(N):
    if A[i] > 0:
        total += A[i]
        cnt += 1
print(math.ceil(total / cnt))
