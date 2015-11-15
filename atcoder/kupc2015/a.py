T = int(input())
for _ in range(T):
    S = input()
    cnt = 0
    tokyo = 0
    kyoto = 0
    i  = 0
    while True:
        tokyo = S[i:].find('tokyo')
        kyoto = S[i:].find('kyoto')
        if tokyo==-1 and kyoto ==-1:
            break
        elif tokyo<0:
            i += kyoto+5
        elif kyoto<0:
            i += tokyo+5
        else:
            i += min(kyoto,tokyo)+5
        cnt += 1
    print(cnt)
