import math
B = int(input())
N = int(input())
C = [int(input()) for i in range(N)]
sum_c = sum(C)

if N == 1:
    print(0)
    exit()

l = 0
r = (sum_c + B) // N + 1
total_l = 0
total_r = 0

for i in range(52): # 52 = ceil((8*log10+log11)/(log3-log2))
    ml = (l * 2 + r) // 3
    mr = (l + r * 2) // 3
    total_l = 0
    total_r = 0
    for c in C:
        total_l += abs(ml - c)
        total_r += abs(mr - c)
    if total_r >= total_l:
        r = mr
    else:
        l = ml
print(min(total_l, total_r))
