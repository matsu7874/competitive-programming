A,B,C = map(int, input().split('.'))
a,b,c = map(int, input().split('.'))
V=101*101*A+101*B+C
v=101*101*a+101*b+c
if V>=v:
    print('YES')
else:
    print('NO')
