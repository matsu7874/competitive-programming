N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(N - 2):
    if A[i] != A[i + 2] and ((A[i] < A[i + 1] and A[i + 1] > A[i + 2]) or (A[i] > A[i + 1] and A[i + 1] < A[i + 2])):
        cnt += 1
print(cnt)
