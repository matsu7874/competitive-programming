import sys
n=int(input())
a=list(map(int, input().split()))
q = []
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
            q.append((i,j))
print(len(q))
for u,v in q:
    print(u,v)

sys.stdout.flush()
dummy = input()