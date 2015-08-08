N = int(input())
depth = 0
n = N
while n>0:
    depth += 1
    n //= 2
depth %= 2
x = 1
turn = 0
player = ['Takahashi', 'Aoki']
while x<=N:
    if turn+depth == 1:
        x = x*2+1
    else:
        x = x*2
    turn = (turn+1)%2
print(player[turn])
