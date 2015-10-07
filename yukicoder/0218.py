import math
a=int(input())
b=int(input())
c=int(input())
if math.ceil(a/b)*2/3 >=  math.ceil(a/c):
    print('YES')
else:
    print('NO')
