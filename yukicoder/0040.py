D = int(input())
A = [int(x) for x in input().split()]
if D < 3:
    print(D)
    print(''.join(str(item) + ' ' for item in A[0:D + 1]))
if D > 2:
    for i in range(3, D + 1)[::-1]:
        A[i - 2] += A[i]
    if A[2] == 0:
        if A[1] == 0:
            print(0)
            print(A[0])
        else:
            print(1)
            print(''.join(str(item) + ' ' for item in A[0:2]))
    else:
        print(2)
        print(''.join(str(item) + ' ' for item in A[0:3]))
