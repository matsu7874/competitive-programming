N = int(input())
A = list(map(int, input().split()))
cnt = 0
l = 0
r = N - 1
while l < r:
    # print(A[l:r + 1])
    if A[l] * 2 + A[l + 1] < A[r - 1] + A[r] * 2:
        cnt += A[l] * 2 + A[l + 1] + 1
        A[l + 2] += A[l] + A[l + 1] + 2
        l += 2
    else:
        cnt += A[r] * 2 + A[r - 1] + 1
        A[r - 2] += A[r] + A[r - 1] + 2
        r -= 2
print(cnt)
