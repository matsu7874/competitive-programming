S = []
for i in range(3):
    S.append(input())

C = [[0 for j in range(26)] for i in range(3)]
L = len(S[0])

for i in range(3):
    for j in range(L):
        C[i][ord(S[i][j]) - ord('A')] += 1

mi = ma = 0
for i in range(26):
    if C[0][i] + C[1][i] < C[2][i]:
        mi = ma = 0
        break
    mi += max(0, C[2][i] - C[1][i])
    ma += min(C[0][i], C[2][i])

if mi <= L // 2 and L // 2 <= ma:
    print('YES')
else:
    print('NO')
