(x, y) = [int(x) for x in input().split()]
k = int(input())
if k>y:
    ans = x+y-(k-y)
else:
    ans = x+k
print(ans)
