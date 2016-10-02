s = '01234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980818283848586878889909192939495969798991'
d = [int(c) for c in s]
L = len(d)
if L != 191:
    print(s)
    exit()

N = int(input())
if not (1 <= N <= 100):
    print(N)
    exit()
for i in range(L):
    d[i] *= N

for i in range(190, 0, -1):
    if d[i] >= 10:
        d[i - 1] += d[i] // 10
        d[i] %= 10

last = len(d)
while d[last - 1] == 0:
    last -= 1

print(str(d[0]) + '.', end='')
for i in range(1, last):
    print(d[i], end='')