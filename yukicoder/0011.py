W = int(input())
H = int(input())
N = int(input())
S = set()
K = set()
for i in range(N):
    (s, k) = map(int, input().split(' '))
    S.add(s)
    K.add(k)
ans = W*len(K) + H*len(S) - N - len(S)*len(K)
print(int(ans))
