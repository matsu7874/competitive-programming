(n,k,m) = [int(x) for x in input().split()]
y = 0
suffix = []
ans = set()
while y<10**n:
    y += k
    suffix.append(y)
cnt = 0
for i in range(10**(n-1), 10**n):
    z = 10
    while z<i*10:
        if i%z in suffix:
            ans.add(i)
            break
        z *= 10
print(len(ans)%m)