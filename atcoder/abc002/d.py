import itertools

NOT_FRIEND = 10000

(N, M) = [int(x) for x in input().split()]
friend = [[NOT_FRIEND for j in range(N)] for i in range(N)]
if M == 0:
    print(1)
    exit()

for _ in range(M):
    (x, y) = [int(x)-1 for x in input().split()]
    friend[x][y] = 1
    friend[y][x] = 1
for i in range(N):
    friend[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            friend[x][y] = min(friend[x][y], friend[x][k]+friend[k][y])
largest_clique = 1
for i in range(2**N):
    clique = []
    are_everyone_friend = True
    for j in range(N):
        if (i & (1<<j)) != 0:
            clique.append(j)
    for pair in itertools.combinations(clique, 2):
        if friend[pair[0]][pair[1]] >= NOT_FRIEND:
            are_everyone_friend = False
            break
    if are_everyone_friend:
        largest_clique = max(largest_clique, len(clique))
print(largest_clique)