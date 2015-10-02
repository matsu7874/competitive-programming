L, R = map(int, input().split())
L = list(map(int, input().split()))
R = list(map(int, input().split()))
cnt = 0
for r in R:
    if r in L:
        L.remove(r)
        cnt += 1
print(cnt)
