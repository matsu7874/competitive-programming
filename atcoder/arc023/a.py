def days_since_epoch(year, month, day):
    # 1年1月1日からの経過日数を求める
    # days_since_epoch(1,1,1)=0
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cnt = day - 1
    for i in range(month - 1):
        cnt += DAYS_IN_MONTH[i]
    cnt += 365 * (year - 1)
    if month <= 2:
        y = year - 1
    else:
        y = year
    cnt += y // 4
    cnt -= y // 100
    cnt += y // 400
    return cnt

y=int(input())
m=int(input())
d=int(input())
print(days_since_epoch(2014,5,17)-days_since_epoch(y,m,d))
