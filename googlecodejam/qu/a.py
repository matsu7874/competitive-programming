T = int(input())
for test_case in range(T):
    Smax, ktmp = input().split()
    Smax = int(Smax)
    k = [int(ktmp[x]) for x in range(Smax+1)]
    audience = 0
    friend = 0
    for i in range(Smax+1):
        if audience+friend < i:
            friend += i-(audience+friend)
        audience += k[i]
    print('Case #'+str(test_case+1)+': '+str(friend))
