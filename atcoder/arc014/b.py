N = int(input())
used = [input()]
for i in range(1, N):
    w = input()
    if used[-1][-1] != w[0] or w in used:
        print(['LOSE', 'WIN'][i % 2])
        exit()
    used.append(w)
print('DRAW')
