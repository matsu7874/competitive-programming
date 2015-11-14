N = int(input())
S = input()
cnt = 0
i = 0
neta = 0
shari = 0
while i < 2 * N - 2:
    t = int(S[i]) + int(S[i + 1])
    if t == 1:
        i += 2
    elif t == 0:
        if shari > 0:
            shari -= 1
            i += 1
        else:
            cnt += 1
            neta += 1
            i += 1
    elif t==2:
        if neta > 0:
            neta -= 1
            i += 1
        else:
            cnt += 1
            shari += 1
            i += 1
print(cnt)
