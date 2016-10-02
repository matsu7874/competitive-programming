n,k,x = map(int, input().split())
p = [[],[]]
t = 0
for i in range(k):
    if i+1 != x:
        a,b = map(int, input().split())
        p[t].append((a-1,b-1)) 
    else:
        _ = input()
        t = 1
c = list(map(int, input().split()))
a = [i+1 for i in range(n)]
for x,y in p[0]:
    a[x],a[y] = a[y],a[x]

for x,y in p[1][::-1]:
    c[x],c[y] = c[y],c[x]
ans = []
for i in range(n):
    if a[i] != c[i]:
        ans.append(i+1)
print(ans[0], ans[1])