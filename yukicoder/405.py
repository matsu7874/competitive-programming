p,q = [float(x) for x in input().split()]
P0 = p*q
P1 = (1-p)*q
P2 = p*(1-q)*q

if P1<P2:
    print('YES')
else:
    print('NO')