yen = [10, 50, 100, 500, 1000]
flg = False
while True:
    p = int(input())
    if p == 0:
        break
    if flg:
        print()
    coins = list(map(int, input().split()))
    pay = [0, 0, 0, 0]
    for i in range(4):
        pay[i] = min(p // yen[i], coins[i])
        p -= pay[i] * yen[i]
        ni = i + 1
        # if p > 0:
        #     while coins[ni] == 0:
        #         ni += 1
        while p > 0 and p % yen[ni] != 0 :
            pay[i] -= 1
            p += yen[i]
    for i in range(4):
        if pay[i] > 0:
            print(yen[i], pay[i])
    flg = True
