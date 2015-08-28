N = int(input())
candidate = {'0':True, '1':True, '2':True, '3':True, '4':True, '5':True, '6':True, '7':True, '8':True, '9':True}
for i in range(N):
    a,b,c,d,r = [x for x in input().split()]
    C = [a,b,c,d]
    if r == 'YES':
        for x in candidate:
            if x not in C:
                candidate[x] = False
    else:
        for x in C:
            if x in candidate:
                candidate[x] = False

for k,v in candidate.items():
    if v:
        print(k)
