N = int(input())
X = [input() for i in range(N)]
cnt = 0
for row in X:
    cnt += row.count('x')
for i in range(9):
    pre = ''
    for j in range(N):
        if pre != 'o' and X[j][i] == 'o':
            cnt += 1
        pre = X[j][i]
print(cnt)
