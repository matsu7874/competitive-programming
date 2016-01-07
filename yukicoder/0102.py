N = list(map(int, input().split()))
win = 0
for n in N:
    win ^= (n % 4)
if win == 0:
    print('Jiro')
else:
    print('Taro')
