import datetime
while True:
    s = input()
    if s == '0':
        exit()
    y = int(s.split('/')[0])
    y_cnt = 0
    while y > 8000:
        y -= 400
        y_cnt += 400
    s = str(y) + '/' + s[s.index('/') + 1:]
    t = datetime.datetime.strptime(s, '%Y/%m/%d %H:%M:%S')
    dt = int(input(), 2)
    dd = dt // 86400
    ds = dt % 86400
    t += datetime.timedelta(days=dd, seconds=ds)
    y = t.year + y_cnt
    print(str(y) + '/' + t.strftime('%m/%d %H:%M:%S'))
