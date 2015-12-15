N = int(input())
A = [int(input()) for i in range(N)]
max_v = A[1] - A[0]

l = 0
r = 1
while r + 1 < N:
    if A[l] > A[r]:
        l = r
    elif A[r] > A[r + 1]:
        max_v = max(max_v, A[r] - A[l])
        if A[l] > A[r + 1]:
            l = r + 1
            r = l
    r += 1
if r<N:
    max_v = max(max_v, A[r] - A[l])
print(max_v)
