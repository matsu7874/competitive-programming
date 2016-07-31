n,l=map(int, input().split())
a=list(map(int, input().split()))

f = -1
for i in range(n-1):
    if a[i] + a[i+1] >= l:
        f = i
        break
if f == -1:
    print('Impossible')
    exit()
print('Possible')
for i in range(1,f+1,1):
    print(i)
for i in range(n-1,f,-1):
    print(i)