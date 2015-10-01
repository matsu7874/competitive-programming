N = int(input())
A = list(map(int, input().split()))
max_length = 1
l = -1
pre = [-1] * 100001
for i in range(N):
    l = max(pre[A[i]]+1,l)
    pre[A[i]] = i
    max_length = max(max_length, i-l+1)
print(max_length)
