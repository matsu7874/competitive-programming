n = int(input())
v = {}
for i in range(n):
    s = input()
    if s in v:
        v[s] += 1
    else:
        v.update({s: 1})
print(sorted([(va, k) for k, va in v.items()])[-1][1])
