N = int(input())
ans = 0
for i in range(N):
    c,d = [int(x) for x in input().split()]
    ans += ((c+1)//2)*d
print(ans%(10**9+7))