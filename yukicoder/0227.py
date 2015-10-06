A=list(map(int, input().split()))
C = [0]*14
for a in A:
    C[a]+=1
if C.count(3)==1 and C.count(2)==1:
    print('FULL HOUSE')
elif C.count(3)==1:
    print('THREE CARD')
elif C.count(2)==2:
    print('TWO PAIR')
elif C.count(2)==1:
    print('ONE PAIR')
else:
    print('NO HAND')
