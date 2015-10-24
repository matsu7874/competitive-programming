N, a = map(int, input().split())
k = int(input())
B = list(map(int, input().split()))
history = [a]

cnt = 1
target = B[a - 1]
while cnt < k:
    if target in history:
        loop_start = history.index(target)
        loop = cnt - loop_start
        print(history[(k - cnt) % loop + loop_start])
        exit()
    else:
        history.append(target)
        target = B[target - 1]
        cnt += 1
else:
    print(target)
