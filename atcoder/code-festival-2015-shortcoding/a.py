a=input
N=int(a())
S=[int(a())for i in range(N)]
print(['Pass','Fail'][sum(S)>=S[0]*2*N])
