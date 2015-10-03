import itertools
A = int(input())
F = [3, 5, 17, 257, 65537]
cnt = 0
for X in itertools.product([True, False], repeat=5):
    f = 1
    for i in range(5):
        if X[i]:
            f *= F[i]
    m = 0
    if f == 1:
        m = 2
    while 2**m * f <= A:
        cnt += 1
        m += 1
print(cnt)
