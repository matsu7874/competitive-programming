n,k = map(int, input().split())
a = []
for i in range(n):
    x,y = map(int, input().split())
    a.append((x,y))
a.sort()
for x,y in a:
    if y >= k:
        print(x)
        exit()
    else:
        k -= y

