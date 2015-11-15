s = input()
length = len(s)
if length % 2 == 0:
    l = length // 2 - 1
    r = length // 2
    flg = True
    while 0 <= l and r < length:
        print(l, s[l], r, s[r])
        if s[l] == s[r]:
            l -= 1
            r += 1
        else:
            flag = False
            break
    if flag:
        print(s[:length // 2] + 'a' + s[length // 2:])
        exit()

    n = -1
    t = ''
    l = length // 2 - 1 - 1
    r = length // 2
    while 0 <= l and r < length:
        print(l, s[l], r, s[r])
        if s[l] == s[r]:
            l -= 1
            r += 1
        elif n == -1:
            n = l
            t = s[r]
            r += 1
        else:
            flag = False
            break
    if flag:
        print(s[:n] + t + s[n:])
        exit()
    n = -1
    t = ''
    l = length // 2 -1
    r = length // 2 + 1
    while 0 <= l and r < length:
        print(l, s[l], r, s[r])
        if s[l] == s[r]:
            l -= 1
            r += 1
        elif n == -1:
            n = r
            t = s[l]
            l += 1
        else:
            flag = False
            break
    if flag:
        print(s[:n] + t + s[n:])
        exit()
