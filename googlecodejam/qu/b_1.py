T = int(input())
for test_case in range(T):
    D = int(input())
    P = [int(x) for x in input().split()]
    P = sorted([p for p in P if p!=0])[::-1]
    minute = 0
    #print('Case #'+str(test_case+1)+': ',P)
    if P.count(9) == 2 and all(x<=3 or x==9 for x in P):
        print('Case #'+str(test_case+1)+': '+str(7))
        continue
    while P != [] and any([p>0 for p in P]):
        minute += 1
        l_P = len(P)
        if l_P == 1:
            if P[0] > 8:
                P.append(P[0]//3)
                P[0] -= P[0]//3
                #print(minute,'Spe3',P)
            elif P[0] > 3:
                P.append(P[0]//2)
                P[0] -= P[0]//2
                #print(minute,'Spe2',P)
            else:
                P[0] -= 1
                #print(minute,'Eat',P)
        else:
            if P[0]>=9 and sum([P.count(x) for x in range(P[0]//3+1,P[0]+1)])+sum([P.count(x) for x in range(2*P[0]//3+1,P[0]+1)])*2-3 < P[0]//3:
                P.append(P[0]//3)
                P[0] -= P[0]//3
                P = sorted([p for p in P if p>0])[::-1]
                #print(minute,'Spe3',P)
            elif sum([P.count(x) for x in range(P[0]//2+1,P[0]+1)])<P[0]//2:
                P.append(P[0]//2)
                P[0] -= P[0]//2
                P = sorted([p for p in P if p>0])[::-1]
                #print(minute,'Spe2',P)
            else:
                P = sorted([p-1 for p in P if p>1])[::-1]
                #print(minute,'Eat',P)
    print('Case #'+str(test_case+1)+': '+str(minute))
    #print('')
