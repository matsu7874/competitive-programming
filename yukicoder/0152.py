def gcd(a, b):
    # 最小公倍数
    while b > 0:
        a, b = b, a % b
    return a

L = int(input())
L = L // 4
cnt = 0
# 原始ピタゴラス数列挙
for m in range(1, int(L**0.5)+1):
    for n in range(m - 1, 0, -2):
        if gcd(m,n) != 1:
            continue
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        if a+b+c <= L:
            cnt += 1
print(cnt)
