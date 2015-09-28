N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(N):
    cnt += A[i] * 2**(N - i - 1)
print(cnt)
