N, M = map(int, input().split())
X = [int(input()) for i in range(M)]
X.sort()
time_min = 0
time_max = int(1.5 * N + 1)
while time_min < time_max:
    time = (time_min + time_max) // 2
    covered = 0
    for x in X:
        if x <= covered:
            if x + time > covered:
                covered = x + time
        else:
            L = x - (covered + 1)
            if L <= time:
                R = max(time - L * 2, (time - L) // 2)
                covered = x + R
            else:
                break
    if covered >= N:
        time_max = time
    else:
        time_min = time + 1
print(time_max)
