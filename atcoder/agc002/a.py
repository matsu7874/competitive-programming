a,b=map(int, input().split())
if b < 0:
    if (b-a+1)%2==0:
        print('Positive')
    else:
        print('Negative')
elif a <= 0 and 0<=b:
    print('Zero')
else:
    print('Positive')

