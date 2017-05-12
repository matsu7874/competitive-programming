x,y = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    if a[i+1]/y < a[i]/x:
        print('NO')
        exit()
print('YES')
