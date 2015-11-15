A=[]
for i in range(1200):
    a,b,p=map(int, input().split())
    A.append((p,a,b))
A.sort()
A.reverse()
for a in A:
    print(a[1],a[2])
