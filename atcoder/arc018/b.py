N = int(input())
P = []
for i in range(N):
    x, y = map(int, input().split())
    P.append((x, y))
cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            s = ((P[j][0] - P[i][0]) * (P[k][1] - P[i][1]) -
                 (P[j][1] - P[i][1]) * (P[k][0] - P[i][0]))
            if s%2==0 and s != 0:
                cnt += 1
print(cnt)
