def solve(p):
    for i in range(2):
        p[i].sort()
    lens = [len(p[i]) for i in range(2)]
    if lens == [0, 1] or lens == [1, 0] or lens == [1, 1]:
        return 2
    if lens[0] == 2:
        if p[0][1][1] - p[0][0][0] <= 720 or 1440 - p[0][1][0] + p[0][0][1] <= 720:
            return 2
        else:
            return 4
    elif lens[1] == 2:
        if p[1][1][1] - p[1][0][0] <= 720 or 1440 - p[1][1][0] + p[1][0][1] <= 720:
            return 2
        else:
            return 4
    else:
        print(p)
    return 0

    # sche = []
    # total = [0, 0]
    # for i in range(len(p[0])):
    #     s,t = p[0][i]
    #     if i == 0 :
    #         if s != 0:
    #             sche.append([0, s, -1])
    #         sche.append([s, t, 0])
    #         total[0] += t-s
    #         continue
    #     if s != sche[-1][1]:
    #         sche.append([sche[-1][1], s, -1])
    #     sche.append([s, t, 0])
    #     total[0] += t-s
    
    # for i in range(len(p[1])):
    #     s,t = p[1][i]
    #     if s != sche[-1][1]:
    #         sche.append([sche[-1][1], s, -1])
    #     sche.append([s, t, 1])
    #     total[1] += t-s

    # print(sche, total)
    return 0

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
