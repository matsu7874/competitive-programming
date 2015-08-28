N,K = [int(x) for x in input().split()]
S = input()

rank = [0 for i in range(N)]
r = 0
for i in range(N):
    if S[i] == '(':
        rank[i] = r
        r += 1
    else:
        r -= 1
        rank[i] = r
if S[K-1] == '(':
    d = 1
else:
    d = -1
t = K-1+d
while True:
    if rank[K-1] == rank[t]:
        print(t+1)
        exit()
    else:
        t += d
