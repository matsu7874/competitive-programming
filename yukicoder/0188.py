DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cnt = 0
for m in range(12):
    for d in range(DAYS_IN_MONTH[m]):
        sum_d = (d + 1) // 10 + (d + 1) % 10
        if m + 1 == sum_d:
            cnt += 1
print(cnt)
