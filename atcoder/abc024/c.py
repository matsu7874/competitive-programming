N,D,K = [int(x) for x in input().split()]
L = []
R = []
S = []
T = []
for _ in range(D):
    l,r = [int(x) for x in input().split()]
    L.append(l)
    R.append(r)
for _ in range(K):
    s,t = [int(x) for x in input().split()]
    S.append(s)
    T.append(t)
for i in range(K):
    p = S[i]
    for d in range(D):
        if L[d]<=p<=R[d]:
            if L[d]<=T[i]<=R[d]:
                print(d+1)
                break
            elif T[i]<=L[d]:
                p = L[d]
            else:
                p = R[d]

