x, y = map(int, input().split())
if x > y:
    x, y = y, x
if x == 3 and y == 4:
    print('snuke')
elif x == 4 and y == 4:
    print('rng')
elif x == 1 and y % 2 == 1:
    print('rng')
elif x == 2 and y % 4 == 2:
    print('rng')
elif x == 3 and y % 4 == 0:
    print('rng')
else:
    print('snuke')
