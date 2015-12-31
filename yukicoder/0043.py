import itertools
N = int(input())
S = [[c for c in input()] for i in range(N)]

best_pos = N
undefined = []
for i in range(0,N):
    for j in range(i+1,N):
        if S[i][j] == '-':
            undefined.append((i,j))
for d in itertools.product('ox',repeat=len(undefined)):
    win = [0 for i in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            if S[i][j] == 'o':
                win[i] += 1
            elif S[i][j] == 'x':
                win[j] += 1
            elif S[i][j] == '-':
                if d[undefined.index((i,j))] == 'o':
                    win[i]+=1
                else:
                    win[j] += 1
    best_pos = min(best_pos, sorted(list(set(win)))[::-1].index(win[0])+1)
print(best_pos)
