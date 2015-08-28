N = int(input())
A = [input().split() for i in range(N)]
candidate = [i for i in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if j in candidate and A[i][j] != 'nyanpass':
            candidate.remove(j)
if len(candidate) == 1:
    print(candidate[0] + 1)
else:
    print(-1)
