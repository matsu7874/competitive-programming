H,W,N,K = [int(x) for x in input().split()]
if H*W%N == K or H*W%N == K-N:
    print('YES')
else:
    print('NO')