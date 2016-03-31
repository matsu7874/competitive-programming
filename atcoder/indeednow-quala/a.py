v = [int(input()) for i in range(2)]
cnt = [0, 0]
for i in range(2):
    while v[i] > 0:
        cnt[i] += 1
        v[i] //= 10
print(cnt[0] * cnt[1])
