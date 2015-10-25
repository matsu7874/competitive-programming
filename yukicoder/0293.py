A, B = map(int, input().split())
t = 10
while t < A or t < B:
    t *= 10
while t > 0:
    a = A % (t * 10) // t
    b = B % (t * 10) // t
    if a==b:
        t//=10
        continue
    elif a==4 and b == 7:
        print(A)
    elif a==7 and b == 4:
        print(B)
    elif a>b:
        print(A)
    else:
        print(B)
    exit()
