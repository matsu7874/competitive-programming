N = int(input())
A = list(input().split())
d = {}
for a in A:
    if a in d:
        d[a] = False
    else:
        d.update({a: True})
cnt = 0
for k, v in d.items():
    if v:
        cnt += 1
print(cnt)
