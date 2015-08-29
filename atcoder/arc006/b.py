N, L = map(int, input().split())

line = [i + 1 for i in range(N)]
for i in range(L):
    S = input()
    for j in range(N - 1):
        if S[2 * j + 1] == '-':
            line[j], line[j + 1] = line[j + 1], line[j]
S = input()
print(line[S.index('o') // 2])
