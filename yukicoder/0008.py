P = int(input())
for i in range(P):
    n, k = [int(x) for x in input().split()]
    if n % (k + 1) == 1:
        print('Lose')
    else:
        print('Win')
