N,K,M,R=map(int, input().split())
S=[int(input()) for i in range(N-1)]
S.sort()
S.reverse()
t = sum(S[:K])
if t >=R*K:
    print(0)
    exit()
else:
    r = R*K-sum(S[:K-1])
    if r>M:
        print(-1)
    else:
        print(r)
