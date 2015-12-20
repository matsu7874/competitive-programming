def day_of_week(y, m, d):
    if m == 1 or m == 2:
        m += 12
        y -= 1
    h = (y + y // 4 - y // 100 + y // 400 + (13 * m + 8) // 5 + d) % 7
    return h

N=int(input())
cnt = 57*(N//400) - 288
h = []
for y in range(1,N%400+1):
    if day_of_week(y,7,23) == 3:
        cnt += 1
print(cnt)
