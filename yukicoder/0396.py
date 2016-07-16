n,m=map(int, input().split())
x,y=map(int, input().split())
xx = x%(2*m)
yy = y%(2*m)
if xx==yy:
    print('YES')
elif (xx+yy)%(2*m) == 1:
    print('YES')
else:
    print('NO')