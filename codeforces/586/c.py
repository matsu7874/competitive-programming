import collections
N = int(input())
line = collections.deque()
for i in range(N):
    v, d, p = map(int, input().split())
    line.append([i, v, d, p])
will_cry = collections.deque()
ok = []
t = 0
while t < N:
    idx, v, d, p = line[t]
    if p >= 0:
        ok.append(idx + 1)
    else:
        t += 1
        continue
    t += 1
    tcnt = 0
    i = 0
    while tcnt < v and t + i < N:
        if line[t + i][3] >= 0:
            line[t + i][3] -= v - tcnt
            if line[t + i][3] < 0:
                will_cry.append(line[t + i][0])
            tcnt += 1
        i += 1
    # print(idx,line, will_cry)

    while will_cry:
        i = will_cry.pop()
        idx, v, d, p = line[i]
        cnt = 0
        j = 0
        while cnt < d and idx + j + 1 < N:
            j += 1
            if line[idx + j][3] < 0:
                continue
            line[idx + j][3] -= d - cnt
            if line[idx + j][3] < 0:
                will_cry.append(idx+j)
            cnt += 1
    # print(idx,line, will_cry,'after')

print(' '.join(list(map(str, ok))))
