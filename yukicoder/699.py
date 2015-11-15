h = [int(x) for x in input().split()]
if (3+h[0]-h[1])%3 == 0:
    print('Drew')
elif (3+h[0]-h[1])%3 == 1:
    print('Lost')
else:
    print('Won')
