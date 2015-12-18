N = int(input())
K = int(input())
S = [i for i in range(N + 1)]
# print('S',S)
for i in range(K):
    x, y = map(int, input().split())
    S[x], S[y] = S[y], S[x]
# print('S',S)
P = [0] + list(map(int, input().split()))
# print('P',P)

G = [P.index(i) for i in range(N+1)]
# print('G',G)

cnt = 0
L = []
for i in range(1,N+1):
    j = S.index(G[i])
    while i<j:
        L.append((j-1,j))
        S[j-1],S[j] = S[j],S[j-1]
        j -= 1
        cnt += 1
# print('S',S)
print(cnt)
for e in L:
    print(*e)
