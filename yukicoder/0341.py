s = input()
max_cnt = 0
cnt = 0
for c in s:
    if c == '…':
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0
print(max(max_cnt, cnt))
