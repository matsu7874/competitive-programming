S = input()
ans = ''
pre = ''
cnt = 0
for c in S:
    if c != pre:
        ans += pre + str(cnt)
        pre = c
        cnt = 1
    else:
        cnt += 1
ans += pre + str(cnt)
print(ans[1:])
