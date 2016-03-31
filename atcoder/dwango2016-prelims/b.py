n=int(input())
k = [1] + list(map(int, input().split())) + [1]
k[0] = k[1]
k[n] = k[n-1]
ans = [1] * n
for i in range(n):
    ans[i] = min(k[i],k[i+1])
print(*ans)
