import math
(R, C) = [int(x) for x in input().split()]
(X, Y) = [int(x) for x in input().split()]
(D, L) = [int(x) for x in input().split()]

MODULUS = 10**9 + 7


def calc(x, y, d, l):
    dis = math.factorial(x * y) // (math.factorial(d) *
                                    math.factorial(l) * math.factorial(x * y - d - l))
    if (x - 1) * y >= d + l:
        dis -= calc(x - 1, y, d, l) * 2
    if x * (y - 1) >= d + l:
        dis -= calc(x, y - 1, d, l) * 2
    return dis

# 部屋のどの位置を区切るか
cnt_partition = (R + 1 - X) * (C + 1 - Y)
# 区切りの中にどう配置するか
if D + L == X * Y:
    cnt_disposition = math.factorial(
        X * Y) // (math.factorial(D) * math.factorial(L))
    print(cnt_disposition * cnt_partition % MODULUS)
else:
    cnt_disposition = calc(X, Y, D, L)
    print(cnt_disposition * cnt_partition % MODULUS)
