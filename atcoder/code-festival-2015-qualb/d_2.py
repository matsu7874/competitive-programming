N = int(input())
if N <= 1000:
    p = []
    for i in range(N):
        s, c = map(int, input().split())
        t = s + c - 1
        j = 0
        while True:
            if j >= len(p):
                break
            if p[j][0] <= s <= p[j][1] and p[j][1] < t:
                t += p[j][1] - s + 1
                s = p[j][0]
                p.pop(j)
                continue
            elif p[j][0] <= s <= p[j][1] and t <= p[j][1]:
                t += p[j][1] - s + 1
                s = p[j][0]
                p.pop(j)
                continue
            elif s < p[j][0] and p[j][1] < t:
                t += p[j][1] - p[j][0] + 1
                p.pop(j)
                continue
            elif s < p[j][0] and p[j][0] <= t <= p[j][1]:
                t += p[j][1] - p[j][0] + 1
                p.pop(j)
                continue
            elif t < p[j][0]:
                break
            j += 1
        p.append((s, t))
        p.sort()
        print(t)
else:
    cells = [-1 for i in range(110001)]
    for i in range(N):
        s, c = map(int, input().split())
        cnt = 0
        while cnt < c:
            if cells[s] == -1:
                cells[s] = s + c - cnt
                cnt += 1
            else:
                ss = s
                s = cells[s]
                cells[ss] = max(cells[ss], ss + c - cnt)
        print(s)
