n = int(input())
V = [int(x) for x in input().split()]
F = [int(x) for x in input().split()]

cnt = 0
for i in range(n):
    if F[i]*2 > V[i]:
        cnt += 1
print(cnt)
