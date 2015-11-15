def calc(a,b):
    minus = (len(a)+len(b)) % 2
    a = a[-1]
    b = b[-1]

    if a == '1':
        f = ['1','i','j','k'][['1','i','j','k'].index(b)]
    if a == 'i':
        f = ['i','-1','k','-j'][['1','i','j','k'].index(b)]
    if a == 'j':
        f = ['j','-k','-1','i'][['1','i','j','k'].index(b)]
    if a == 'k':
        f = ['k','j','-i','-1'][['1','i','j','k'].index(b)]
    
    if len(f)==2 and minus==1:
        return f[-1]
    elif len(f)==1 and minus==1:
        return '-'+f
    else:
        return f

T = int(input())
for test_case in range(T):
    L,X = [int(x) for x in input().split()]
    S = input()
    S = S*X
    ans = '1'
    flg = [False, False, False]
    lenS = len(S)
    for i in range(lenS):
        print(ans,S[i],calc(ans,S[i]),flg)
        ans = calc(ans,S[i])
        if flg[0]:
            if flg[1]:
                pass
            elif ans=='j':
                flg[1] = True
                ans = '1'
        elif ans == 'i':
            flg[0] = True
            ans = '1'
    if ans == 'k':
        flg[2] = True
    print(flg)
    if all(flg):
        print('Case #'+str(test_case+1)+': YES')
    else:
        print('Case #'+str(test_case+1)+': NO')