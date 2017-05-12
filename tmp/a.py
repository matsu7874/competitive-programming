M, N = map(int, input().split())
s = []
for i in range(M):
    s.append(int(input()))
p = []
for i in range(N):
    p.append(int(input()))

v = set()
for i in range(N):
    for j in range(N):
        v.add(p[i] * p[j])
v = sorted(list(v))
len_v = len(v)
for i in range(M):
    if s[i] <= v[0]:
        print(v[0] - s[i])
        continue
    l = 0
    r = len_v
    while l+1 < r:
        m = (l+r)//2
        if v[m] < s[i]:
            l = m
        else:
            r = m

    print(v[r] - s[i])
