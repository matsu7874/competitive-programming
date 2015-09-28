N = int(input())
r = 0
b = 0
for i in range(N):
    S = input()
    for c in S:
        if c == 'R':
            r += 1
        elif c == 'B':
            b += 1
if r > b:
    print('TAKAHASHI')
elif b > r:
    print('AOKI')
else:
    print('DRAW')
