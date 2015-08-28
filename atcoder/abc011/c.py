N = int(input())
NG = [int(input()) for i in range(3)]
if N in NG:
    print('NO')
    exit()
rest = 100
t = N
while rest > 0 and t > 0:
    if t < 3 or t - 3 in NG:
        if t < 2 or t - 2 in NG:
            if t - 1 in NG:
                break
            else:
                t -= 1
        else:
            t -= 2
    else:
        t -= 3
    rest -= 1

if t == 0:
    print('YES')
else:
    print('NO')
