import itertools
N=int(input())
S=[input() for i in range(N)]
T=list(''.join(s) for s in itertools.permutations(S,2))
T.sort()
print(T[0])
