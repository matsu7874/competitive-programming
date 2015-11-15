T = int(input())
for test_case in range(T):
    D = int(input())
    P = [int(x) for x in input().split()]
    P = sorted([p for p in P if p!=0])[::-1]
    minute = 0
    print('Case #'+str(test_case+1)+': ',P)
    while P != [] and any([p>0 for p in P]):
        minute += 1
        if P[0]>=9 and (all([P[x]<=P[0]//3 for x in range(1,len(P))]) or sum():
            t = P[0]
            P = P[1:]
            P.append(t//3)
            P.append(t-t//3)
            P = sorted([p for p in P if p>0])[::-1]
            print(minute,'Spe',P)
        elif P[0]>3 and P[0]>len(P) and (P.count(P[0])<P[0]//2):
            P.append(P[0]//2)
            P[0] -= P[0]//2
            P = sorted([p for p in P if p>0])[::-1]
            print(minute,'Spe',P)
        else:
            P = sorted([p-1 for p in P if p>1])[::-1]
            print(minute,'Nor',P)
    print('Case #'+str(test_case+1)+': '+str(minute))
    print('')
