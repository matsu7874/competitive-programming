N, T = map(int, input().split())
Z = []
total = 0
for i in range(N):
    a, b = map(int, input().split())
    total += a
    Z.append(a - b)
Z.sort()
Z.reverse()
cnt = 0
while total > T and cnt<N:
    total -= Z[cnt]
    cnt += 1
if total > T:
    print(-1)
else:
    print(cnt)
