N = int(input())
ok = 0
miss = 0
for i in range(N):
    t, s = input().split()
    t = int(t)
    l = len(s)
    ok += min(12 * t // 1000, l)
    miss += l - min(12 * t // 1000, l)
print(ok, miss)
