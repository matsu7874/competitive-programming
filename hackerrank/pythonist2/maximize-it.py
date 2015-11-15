K,M = map(int, input().split())
N = []
for i in range(K):
    N.append(list(set([(int(x)**2)%M for x in input().split()])))
L = [len(N[i]) for i in range(K)]

max_value = 0
T = [0 for i in range(K)]
up = False
cur = K-1
while T[0]<L[0]:
    if up:
        T[cur] = 0
        cur -= 1
        T[cur] += 1
        if T[cur] >= L[cur]:
            up = True
        else:
            up = False
            cur = K-1
    else:
        max_value = max(max_value, sum(N[i][T[i]] for i in range(K))%M)
        T[cur] += 1
        if T[cur] >= L[cur]:
            up = True
print(max_value)
