def solve(p):
    sche = []
    total = [0, 0]
    P = []
    for i in range(2):
        for s,e in p[i]:
            P.append([s,e,i])
    P.sort()
    sche = []
    sche.append([0, P[0][0], -1])
    for s,e,x in P:
        if s != sche[-1][1]:
            sche.append([sche[-1][1], s, -1])
        sche.append([s, e, x])

    if sche[-1][1] != 1440:
        sche.append([sche[-1][1], 1440 + P[0][0], -1])
    sche.pop(0)
    for s,e,x in sche:
        if x >= 0:
            total[x] += e-s
    # print(sche, total)
    i = 1
    while i+1 < len(sche):
        if sche[i][2] == -1 and sche[i-1][2] == sche[i+1][2] and (total[sche[i+1][2]] + sche[i][1]-sche[i][0])<=720:
            total[sche[i+1][2]] += sche[i][1]-sche[i][0]
            sche[i-1] = [sche[i-1][0], sche[i+1][1], sche[i+1][2]]
            sche.pop(i+1)
            sche.pop(i)
        else:
            i += 1
    sche.append(sche[0])
    sche.append(sche[1])
    cnt = 0
    for i in range(0, len(sche)-2):
        if sche[i][2] == -1:
            pass
        elif sche[i][2] == sche[i+1][2]:
            pass
        elif sche[i+1][2] != -1:
            cnt += 1
        else:
            cnt += 1
            sche[i+1][2] = 1-sche[i][2] 
        # else:
            # cnt += 2


    # print(sche, total)
    return cnt

def print_answer(t, ans):
    tmpl = 'Case #{0}: {1}'
    print(tmpl.format(t+1, ans))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        Ac, Aj = map(int, input().split())
        p = [[], []]
        for i in range(Ac):
            s, e = map(int, input().split())
            p[0].append((s, e))
        for i in range(Aj):
            s, e = map(int, input().split())
            p[1].append((s, e))
        ans = solve(p)
        print_answer(_, ans)
