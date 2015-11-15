import itertools

N, M = map(int, input().split())
score = [[0 for j in range(N)] for i in range(N)]
for i in range(M):
    a, b, s = map(int, input().split())
    score[a][b] = s
# max_score = 0
# for p in itertools.permutations(range(N)):
#     s = 0
#     for i in range(N - 1):
#         for j in range(i + 1, N):
#             s += score[p[i]][p[j]]
#     max_score = max(max_score, s)
# print(max_score)

greed = []
for i in range(N):
    max_s = 0
    for j in range(len(greed)+2):
        s = score[]
